import streamlit as st
import os
import pandas as pd
from backend.model import read_name_from_image, crop_and_read_names, save_to_csv, count_names_in_csv

# สร้างโฟลเดอร์สำหรับอัปโหลดถ้าไม่มี
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

CSV_FILE = 'backend/names.csv'  # แก้ไขให้ตรงตามพาธไฟล์

def upload():
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

