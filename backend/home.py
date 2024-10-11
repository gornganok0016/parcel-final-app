import streamlit as st
import os
import pandas as pd
from streamlit_option_menu import option_menu
from model import read_name_from_image, crop_and_read_names, save_to_csv, count_names_in_csv

# สร้างโฟลเดอร์สำหรับอัปโหลดถ้าไม่มี
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

CSV_FILE = 'D:/POSTOAPP2/backend/names.csv'  # แก้ไขให้ตรงตามพาธไฟล์

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
    # สร้าง Navigation Bar ด้านบน
    st.markdown("""
        <style>
        .navbar {
            display: flex;
            justify-content: space-around;
            background-color: #f0f0f0;
            padding: 10px;
        }
        .navbar a {
            text-decoration: none;
            color: black;
            padding: 10px;
            border-radius: 5px;
        }
        .navbar a:hover {
            background-color: #ddd;
        }
        </style>
        <div class="navbar">
            <a href="#" onclick="window.location.reload(); st.session_state['page'] = 'home';">หน้าแรก</a>
            <a href="#" onclick="window.location.reload(); st.session_state['page'] = 'upload';">หน้าอัปโหลด</a>
            <a href="#" onclick="window.location.reload(); st.session_state['page'] = 'chat';">Chatbot</a>
        </div>
    """, unsafe_allow_html=True)

    # จัดการการนำทาง
    if 'page' not in st.session_state:
        st.session_state['page'] = 'home'  # กำหนดค่าเริ่มต้น

    if st.session_state['page'] == 'upload':
        admin()
    elif st.session_state['page'] == 'chat':
        chat()
    else:
        home()
        
if __name__ == "__main__":
    main()
