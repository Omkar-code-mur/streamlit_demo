from streamlit_webrtc import webrtc_streamer
import av
import cv2

import streamlit as st

st.slider("Threshold1",0,1000)
st.slider("Threshold2",0,100)

def callback(frame: av.VideoFrame) -> av.VideoFrame:
    img = frame.to_ndarray(format="bgr24")
    img = cv2.Canny(img,100,200)
    img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
    
    
    return av.VideoFrame.from_ndarray(img,format="bgr24")
webrtc_streamer(

    key="sample",    
    video_frame_callback=callback
    )
