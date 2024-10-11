import streamlit as st

def show_home():
    st.title("หน้าแรก")
    st.write("ยินดีต้อนรับสู่แอปพลิเคชันของเรา!")

def main():
    st.sidebar.title("เมนู")
    page = st.sidebar.radio("เลือกหน้า:", ["หน้าอัปโหลด", "Chatbot"])

    elif page == "หน้าอัปโหลด":
        from pages.upload import show_upload  # นำเข้าฟังก์ชันจาก upload.py
        show_upload()
    elif page == "Chatbot":
        from pages.chat import show_chat  # นำเข้าฟังก์ชันจาก chat.py
        show_chat()

# ตรวจสอบว่าเป็นการรันสคริปต์โดยตรง
if __name__ == "__main__":
    main()

