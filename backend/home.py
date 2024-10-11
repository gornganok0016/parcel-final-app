import streamlit as st
import os
import pandas as pd
from model import read_name_from_image, crop_and_read_names, save_to_csv, count_names_in_csv
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


# สร้างโฟลเดอร์สำหรับอัปโหลดถ้าไม่มี
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

CSV_FILE = 'D:/POSTOAPP2/backend/names.csv'  # แก้ไขให้ตรงตามพาธไฟล์

# Firebase initialization
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# กำหนดค่าเริ่มต้นให้กับ session state
if 'is_logged_in' not in st.session_state:
    st.session_state.is_logged_in = False

if 'signup' not in st.session_state:
    st.session_state.signup = False

# ฟังก์ชันสำหรับหน้า Login
def login():
    st.title("Login")
    
    email = st.text_input("Email", key="email_input")
    password = st.text_input("Password", type="password", key="password_input")
    
    if st.button("Login"):
        try:
            # ทำการล็อกอินผู้ใช้
            user = auth.sign_in_with_email_and_password(email, password)
            st.session_state.is_logged_in = True  # เปลี่ยนสถานะเป็นล็อกอินแล้ว
            st.success("Login สำเร็จ!")  # แสดงข้อความสำเร็จ
            st.experimental_rerun()  # เริ่มต้นการทำงานใหม่
        except Exception as e:
            error_message = str(e)
            st.error("Login ไม่สำเร็จ กรุณาตรวจสอบข้อมูลอีกครั้ง.")
            st.warning("อีเมลนี้ไม่มีในระบบ! กรุณาลงทะเบียนที่นี่")  # ลบลิงก์ Markdown
             # เพิ่มปุ่มให้ผู้ใช้สามารถลงทะเบียนได้
            if st.button("Sign Up"):
                st.session_state.signup = True  # เปลี่ยนสถานะเป็นต้องการลงทะเบียน
                st.experimental_rerun()  # เริ่มต้นการทำงานใหม่


# ฟังก์ชันสำหรับหน้า Sign Up
def sign_up():
    st.title("Sign Up")
    
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Sign Up"):
        try:
            # ทำการสร้างบัญชีผู้ใช้
            auth.create_user_with_email_and_password(email, password)
            st.success("Sign Up สำเร็จ! กรุณาเข้าสู่ระบบ.")
            st.session_state.signup = False  # รีเซ็ตสถานะ signup
            st.experimental_rerun()  # เริ่มต้นการทำงานใหม่
        except Exception as e:
            st.error("Sign Up ไม่สำเร็จ กรุณาตรวจสอบข้อมูลอีกครั้ง: " + str(e))
# ฟังก์ชันสำหรับหน้าแรก
def home():
    st.title("หน้าแรก")
    st.write("ยินดีต้อนรับสู่แอปพลิเคชันของเรา!")

# ฟังก์ชันสำหรับหน้าอัปโหลด
def admin():
    st.title("หน้าอัปโหลด")
    uploaded_file = st.file_uploader("อัปโหลดไฟล์", type=['jpg', 'png'])
    
    if uploaded_file is not None:
        image_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
        
        # บันทึกไฟล์ภาพ
        with open(image_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # ตรวจจับชื่อจากภาพ
        detected_names, boxes = read_name_from_image(image_path)

        if detected_names:
            cropped_names = crop_and_read_names(image_path, boxes)
            save_to_csv(cropped_names)

            # แสดงผลลัพธ์
            st.write("Detected Names: ", ", ".join(detected_names))
            st.write("Cropped Names: ", ", ".join(cropped_names))
            st.write("Name Counts: ", count_names_in_csv().to_dict(orient='records'))
        else:
            st.warning("ไม่พบชื่อในภาพ")

# ฟังก์ชันสำหรับหน้า Chatbot
def chat():
    st.title("Chatbot")
    question = st.text_input("ถามคำถามของคุณที่นี่:")
    
    if st.button("ส่งคำถาม"):
        answer = handle_chat(question)
        st.write(answer)

def handle_chat(question):
    # ตรวจสอบว่าคำถามมีอยู่ใน CSV หรือไม่
    if question:
        if check_question_in_csv(question):
            return f"The question '{question}' is found in the CSV."
        else:
            return f"The question '{question}' is not found in the CSV."
    return "กรุณาถามคำถามที่ถูกต้อง."

def check_question_in_csv(question):
    # อ่านข้อมูลจากไฟล์ CSV
    try:
        df = pd.read_csv(CSV_FILE)  # อ่านไฟล์ CSV
        return question in df['name'].values
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return False

# ฟังก์ชันหลัก
def main():
    # กำหนดค่าเริ่มต้นให้กับ session state
    if 'is_logged_in' not in st.session_state:
        st.session_state.is_logged_in = False

    if 'signup' not in st.session_state:
        st.session_state.signup = False

    if not st.session_state.is_logged_in:  # ถ้ายังไม่ได้ล็อกอิน
        if st.session_state.signup:  # ถ้าต้องการไปที่หน้า Sign Up
            sign_up()  # แสดงหน้า Sign Up
        else:
            login()  # แสดงหน้า Login
    else:
        # เมนูสำหรับหน้าอื่น ๆ เมื่อผู้ใช้ล็อกอินสำเร็จ
        st.sidebar.title("เมนู")
        page = st.sidebar.radio("เลือกหน้า:", ["หน้าแรก", "หน้าอัปโหลด", "Chatbot"])

        if page == "หน้าแรก":
            home()
        elif page == "หน้าอัปโหลด":
            admin()
        elif page == "Chatbot":
            chat()

if __name__ == "__main__":
    main()

