
# Yolov5-Deployment-on-Streamlit-Realtime
This repository will deploy your yolov5 object detection model on streamlit.

I have used my pre-trained weights on a custom dataset to detect if a person is wearing a mask or not. These weights are saved with
    pytorch extension.
```
last.pt
```
Clone this repository using
```
git clone https://github.com/HassanBinAli/Yolov5-Deployment-on-Streamlit-Realtime  # clone
cd Yolov5-Deployment-on-Streamlit-Realtime
```



## Functions
The app has three tabs

    1)	Upload Image: will allow you to upload image and make prediction.
    2)	Capture Image: will allow you to capture image using your webcam and make prediction.
    3)	Realtime: will allow you to use your webcam to predict in real time.

## Install Dependencies
Install the following Dependencies using Powershell or Command Prompt
```
pip install streamlit
pip install streamlit-webrtc
pip install av
```
## Files
    1)	Single_instance.py: is the file that takes one image and makes the prediction unlike the command-line interfaces commonly used for yolov5 predictions.
    2)	App.py: is the streamlit app that runs locally.
    

## How to run app
After done cloning the repository, open the terminal in the folder
   
    Yolov5-Deployment-on-Streamlit-Realtime
and run the following command in the terminal
```
streamlit run app.py
```
## How it looks when running
### Tab 1
The first tab which allows you to upload an image and make prediction
![Capture0](https://github.com/HassanBinAli/Yolov5-Deployment-on-Streamlit-Realtime/assets/87352841/f76fa40f-c3c8-4ad4-8f40-3555ca055874)

### Tab 2
The second tab which allows you to capture an image and make prediction
![Capture1](https://github.com/HassanBinAli/Yolov5-Deployment-on-Streamlit-Realtime/assets/87352841/292e157e-28f7-460f-a945-fc71735e4097)

### Tab 3
The third tab which allows you to make predictions in real-time
https://github.com/HassanBinAli/Yolov5-Deployment-on-Streamlit-Realtime/assets/87352841/a4812ece-139a-4690-9c2f-b0e0fc3468a2

## Final thoughts
I hope it was helpful. The Realtime tab takes some time because it executes the code from start. If anybody has a better solution, please share.




