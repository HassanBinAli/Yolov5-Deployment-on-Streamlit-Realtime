import streamlit as st
import numpy as np
import cv2
import torch
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
import av
# from Single_Instance import draw_bounding_boxes


model = torch.hub.load('ultralytics/yolov5','custom', 'last.pt')  # custom trained model

class_label = {
    0: "Mask",
    1: "No Mask"
}

def draw_bounding_boxes(pred_tensor, result):
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.7
    size_of_tensor = list(pred_tensor.size())
    rows = size_of_tensor[0]
    for i in range(0, rows):
        cv2.rectangle(result, (int(pred_tensor[i,0].item()), int(pred_tensor[i,1].item())), 
        (int(pred_tensor[i,2].item()), int(pred_tensor[i,3].item())), (0, 0, 255), 2)

        text = class_label[int(pred_tensor[i,5].item())] +" " + str(round(pred_tensor[i,4].item(), 2))

        image = cv2.putText(result, text, (int(pred_tensor[i,0].item())+5, int(pred_tensor[i,1].item())), 
        font, fontScale, (0, 0, 255), 2)
        
    return result


tab1, tab2, tab3 = st.tabs(["Upload Image", "Capture Image", "Real Time"])

with tab1:
    test_image = st.file_uploader('Face Image', type=['jpg', 'png','jpeg'] )
    col1, col2 = st.columns(2)
    if test_image is not None:
        # Convert the file read to the bytes array.
        file_bytes = np.asarray(bytearray(test_image.read()), dtype=np.uint8)
        # Converting the byte array into opencv image. 0 for grayscale and 1 for bgr
        test_image_decoded = cv2.imdecode(file_bytes,1) 
        col1.subheader('Uploaded Test Image')
        col1.image(test_image_decoded, channels = "BGR")
        prediction = model(test_image_decoded)
        result_img = draw_bounding_boxes(prediction.xyxy[0], test_image_decoded)
        col2.subheader('Predicted Image')
        col2.image(result_img, channels = "BGR")

   
with tab2:
    
    img_camera = st.camera_input("Capture Image")

    # print(img_clicked)
    if img_camera is not None:
        # Convert the file read to the bytes array.
        file_bytes = np.asarray(bytearray(img_camera.read()), dtype=np.uint8)
        # Converting the byte array into opencv image. 0 for grayscale and 1 for bgr
        test_image_decoded = cv2.imdecode(file_bytes,1) 
        prediction = model(test_image_decoded)
        result_img = draw_bounding_boxes(prediction.xyxy[0], test_image_decoded)
        st.subheader('Predicted Image')
        st.image(result_img, channels = "BGR")
    

with tab3:
    
    class VideoProcessor:
        def recv(self, frame):
            img = frame.to_ndarray(format="bgr24")
            prediction = model(img)
            print(prediction)
            result_img = draw_bounding_boxes(prediction.xyxy[0], img)
            #return img
            return av.VideoFrame.from_ndarray(result_img, format="bgr24")

    RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]})
    webrtc_ctx = webrtc_streamer(
        key="WYH",
        mode=WebRtcMode.SENDRECV,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={"video": True, "audio": False},
        video_processor_factory=VideoProcessor,
        async_processing=True,
    )


