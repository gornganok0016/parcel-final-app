import streamlit as st
import pyrebase

def change_colors():
    style = """
        <style>
            #login {
                color: #333366;  /* เปลี่ยนสีของคำว่า Login */
            }
            input[type="Email"], input[type="Password"] {
                color: #333366;  /* สีข้อความในฟิลด์ input */
            }
            .st-emotion-cache-bm2z3a {
                background-color: #f0f0f0;  /* สีพื้นหลัง */
            }
            .st-emotion-cache-h4xjwg{
                background-color: #ff5f5f;  /* สีพื้นหลัง */
            }
            .stText {
                color: #333366;  /* สีของตัวอักษร */
            }
            .stButton>button {
                background-color: #f9e75e;  /*  */
                color: #333366;  /* สีของตัวอักษรในปุ่ม */
            }
            .stButton>button:hover {
                background-color: #ff5f5f;  /* สีของปุ่มเมื่อชี้เมาส์ */
            }
            footer {
                visibility: hidden;  /* ซ่อนฟุตเตอร์ */
            }
            #MainMenu {
                visibility: hidden;  /* ซ่อนเมนูหลัก */
            }
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)


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

allowed_email = "admin@adminbydorm.com"
allowed_password = "admin1234"

def login():
    change_colors()
    st.title("Login")

    if "login_status" not in st.session_state:
        st.session_state.login_status = None  # ตั้งค่าเริ่มต้นเป็น None

    
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            st.session_state.login_status = "success"
        except:
            st.error("Login ไม่สำเร็จ กรุณาตรวจสอบข้อมูลอีกครั้ง.")
            st.session_state.current_page = "Sign Up"  # เปลี่ยนไปยังหน้า Home
            st.switch_page("pages/2_SignUp.py")  # สลับไปยังหน้า Home

    if st.session_state.login_status == "success":
         st.success("Login สำเร็จ!")
         st.session_state.current_page = "home"  # เปลี่ยนไปยังหน้า Home
         st.switch_page("pages/4_Chatbot.py")  # สลับไปยังหน้า Home

    if st.button("Login admin"):
        # ตรวจสอบว่า email และ password ตรงกับที่กำหนดไว้หรือไม่
        if email == allowed_email and password == allowed_password:
            try:
                user = auth.sign_in_with_email_and_password(email, password)
                st.session_state.email = email  # เก็บอีเมลลงใน session state
                st.session_state.login_status = "success"
            except:
                st.error("Login ไม่สำเร็จ กรุณาตรวจสอบข้อมูลอีกครั้ง.")
        else:
            st.error("Email หรือ Password ไม่ถูกต้อง.")

    if st.session_state.login_status == "success":
         st.success("Login สำเร็จ!")
         st.session_state.current_page = "Admin"  # เปลี่ยนไปยังหน้า Home
         st.switch_page("pages/3_Admin.py")  # สลับไปยังหน้า Home

        
    
if __name__ == "__main__":
    login()

