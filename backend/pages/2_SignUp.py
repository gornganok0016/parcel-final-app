import streamlit as st
import os
import pandas as pd
from model import read_name_from_image, crop_and_read_names, save_to_csv, count_names_in_csv
import pyrebase
from streamlit_chat import message

# Firebase config
firebaseConfig = {
    'apiKey': "AIzaSyCt7JaHwmHCS9Lm_hiZQv1B2XM_1eR4zPM",
    'authDomain': "posto-ai-app.firebaseapp.com",
    'databaseURL': "https://YOUR_PROJECT_ID.firebaseio.com",
    'projectId': "posto-ai-app",
    'storageBucket': "posto-ai-app.appspot.com",
    'messagingSenderId': "408360408985",
    'appId': "1:408360408985:web:55ec7842c40203f28c6508",
    'measurementId': "G-HL46XMRBKM"
}

# Firebase initialization
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

st.title("Sign Up")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
      
if st.button("Sign Up"):
    st.success("Sign Up สำเร็จ!")
    st.session_state.current_page = "login"  # เปลี่ยนไปยังหน้า Login
    st.switch_page("1_Login")  # สลับไปยังหน้า Login
