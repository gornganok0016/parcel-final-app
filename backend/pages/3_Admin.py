import streamlit as st
import os
import pandas as pd
from model import read_name_from_image, crop_and_read_names, save_to_csv, count_names_in_csv

def change_colors():
    style = """
        <style>
            #upload-parcel-image {
                color: #333366;  /* เปลี่ยนสีของคำว่า Login */
            }
            .st-emotion-cache-bm2z3a {
                background-color: #f0f0f0;  /* สีพื้นหลัง */
            }
            .st-emotion-cache-h4xjwg{
                background-color: #ff5f5f;  /* สีheader */
            }
            st-emotion-cache-1dp5vir{
                background-color: #ff5f5f;  /* header */
            }
            .st-emotion-cache-0 e1f1d6gn0{
                color: #333366;
            }
            .stText {
                color: #333366;  /* สีของตัวอักษร */
            }
            .st-emotion-cache-1erivf3{
                background-color: #333366;  /* สี upload */
            }
            st-emotion-cache-15hul6a{
                background-color: #333366;  /* สี upload */
            }
            .stButton>button {
                background-color: #f9e75e;  /*  */
                color: #333366;  /* สีของตัวอักษรในปุ่ม */
            }
            .stButton>button:hover {
                background-color: #f9e75e;  /* สีของปุ่มเมื่อชี้เมาส์ */
            }
        
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)

def check_login():
    if "login_status" not in st.session_state or not st.session_state.login_status:
        st.warning("กรุณา Login ก่อนเข้าหน้าอื่น")
        st.session_state.current_page = "Login"  # เปลี่ยนไปยังหน้า Home
        st.switch_page("pages/1_Login.py")  # สลับไปยังหน้า Home

    if "email" not in st.session_state or st.session_state.email != "admin@adminbydorm.com":  # เปลี่ยนเป็นบัญชีที่อนุญาต
        st.warning("คุณไม่มีสิทธิ์เข้าถึงหน้านี้")
        st.stop()  # หยุดการทำงานถ้าผู้ใช้ไม่มีสิทธิ์

def logout():
    if "login_status" in st.session_state:
        st.session_state.login_status = False
    if "email" in st.session_state:
        st.session_state.email = None  # ลบอีเมลออกจาก session
    st.success("Logout สำเร็จ!")
    st.session_state.current_page = "login"  # เปลี่ยนไปที่หน้า Login
    st.switch_page("pages/1_Login.py")  # สลับไปยังหน้า Home
    st.session_state['past'] = []
    st.session_state['generated'] = []
    
    st.experimental_rerun()  # รีเฟรชหน้า

# สร้างโฟลเดอร์สำหรับอัปโหลดถ้าไม่มี
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

CSV_FILE = 'backend/names.csv'  # แก้ไขให้ตรงตามพาธไฟล์


# กำหนด URL ของรูปโปรไฟล์
user_avatar = "https://firebasestorage.googleapis.com/v0/b/posto-ai-app.appspot.com/o/user.png?alt=media&token=f22ea9fc-4de4-4ed9-801b-4a2875312905"  # URL ของรูปโปรไฟล์ผู้ใช้
bot_avatar = "https://firebasestorage.googleapis.com/v0/b/posto-ai-app.appspot.com/o/robot.png?alt=media&token=99e37f4c-dbef-4d07-86a5-75e70585ac54"    # URL ของรูปโปรไฟล์ Chatbot

def Admin():
    change_colors()
    check_login()  # ตรวจสอบการล็อกอิน
    st.title("Upload Parcel Image")
    uploaded_file = st.file_uploader("Select Files", type=['jpg', 'png'])
        
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
    if st.button("Logout"):
        logout()  # เรียกฟังก์ชัน logout

if __name__ == "__main__":
    Admin()
