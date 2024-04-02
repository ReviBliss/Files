import streamlit as st
import pandas as pd

st.subheader('Uploading CSV file')
file = st.file_uploader('Upload CSV file', type=['csv', 'xls'])
st.write(file)

if (file is not None):
    st.subheader('Loading csv file')
    df = pd.read_csv(file)
    if (df is not None):
        st.table(df.head())
#         st.write(df)

st.subheader('Show Image directly')
st.image("C:/Users/41782/Desktop/Streamlit/img.png")

st.subheader('Uploading image file')
img_file = st.file_uploader('Upload Image file', type = ['png', 'jpeg'])
if (img_file is not None):
    st.image(img_file)

st.subheader('Uploading vieo file')
video_file = st.file_uploader('Upload video file', type = ['mp4', 'mkv'])
if (video_file is not None):
    st.video(video_file, start_time=0)

st.subheader('Uploading audio file')
audio_file = st.file_uploader('Upload Audio file', type = ['mp3', 'wav'])
if (audio_file is not None):
    st.audio(audio_file.read())