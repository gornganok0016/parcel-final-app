import streamlit as st

# ฟังก์ชันสำหรับหน้าแรก
def home():
    st.title("หน้าแรก")
    st.write("ยินดีต้อนรับสู่แอปพลิเคชันของเรา!")

# ฟังก์ชันสำหรับหน้าอัปโหลด
def admin():
    st.title("หน้าอัปโหลด")
    uploaded_file = st.file_uploader("อัปโหลดไฟล์", type=['jpg', 'png'])
    if uploaded_file is not None:
        st.image(uploaded_file, caption="ภาพที่อัปโหลด", use_column_width=True)

# ฟังก์ชันสำหรับหน้า Chatbot
def chat():
    st.title("Chatbot")
    question = st.text_input("ถามคำถามของคุณที่นี่:")
    if st.button("ส่งคำถาม"):
        st.write(f"คุณถาม: {question}")

# ฟังก์ชันหลัก
def main():
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
