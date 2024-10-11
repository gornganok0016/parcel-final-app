import streamlit as st
import pyrebase


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

def login():
    st.title("Login")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.success("Login สำเร็จ!")
            st.session_state.current_page = "home"  # เปลี่ยนไปยังหน้า Home
            st.switch_page("5_Home")  # สลับไปยังหน้า Home
        except:
            st.error("Login ไม่สำเร็จ กรุณาตรวจสอบข้อมูลอีกครั้ง.")

if __name__ == "__main__":
    login()

