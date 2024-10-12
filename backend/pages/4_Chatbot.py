import streamlit as st
import pandas as pd
from streamlit_chat import message
import os

def check_login():
    if "login_status" not in st.session_state or not st.session_state.login_status:
        st.warning("กรุณา Login ก่อนเข้าหน้าอื่น")
        st.session_state.current_page = "Login"
        st.switch_page("pages/1_Login.py")

# กำหนดค่าเริ่มต้นสำหรับ messages
st.session_state.setdefault('past', [])
st.session_state.setdefault('generated', [])

# สร้างโฟลเดอร์สำหรับอัปโหลดถ้าไม่มี
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

CSV_FILE = 'backend/names.csv'
def change_colors():
    style = """
        <style>
            # #upload-parcel-image {
            #     color: #333366;  /* เปลี่ยนสีของคำว่า Login */
            # }
            .st-emotion-cache-bm2z3a {
                background-color: #f0f0f0;  /* สีพื้นหลัง */
            }
            .st-emotion-cache-h4xjwg{
                background-color: #ff5f5f;  /* สีheader */
            }
            st-emotion-cache-1dp5vir{
                background-color: #ff5f5f;  /* header */
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

def chat():
    change_colors()
    check_login() 

    # ฟังก์ชันสำหรับการตรวจสอบคำถามใน CSV
    def check_question_in_csv(question):
        try:
            df = pd.read_csv(CSV_FILE)
            return question in df['name'].values
        except Exception as e:
            st.error(f"เกิดข้อผิดพลาดในการอ่านไฟล์ CSV: {e}")
            return False
    
    # ฟังก์ชันที่จัดการคำถาม
    def handle_chat(question):
        if question:
            if check_question_in_csv(question):
                return f"✅ พัสดุของ {question} มาถึงแล้วครับ"
            else:
                return f"❌ พัสดุของ {question} ยังไม่มาถึงครับ"
        return "🚫 กรุณาใส่ชื่อผู้รับพัสดุ"
    
    # ฟังก์ชันสำหรับการส่งข้อความ
    def on_input_change():
        user_input = st.session_state.user_input
        if user_input:
            st.session_state.past.append(user_input)
            answer = handle_chat(user_input)
            st.session_state.generated.append(answer)
            st.session_state.user_input = ""

    # ตรวจสอบการตั้งค่า session_state
    if 'past' not in st.session_state:
        st.session_state['past'] = []

    if 'generated' not in st.session_state:
        st.session_state['generated'] = []

    # แสดงข้อความใน container
    chat_placeholder = st.empty()

    # ส่วนที่แสดงข้อความ
    with chat_placeholder.container():
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=f"user_{i}")
            message(st.session_state['generated'][i], key=f"bot_{i}")

    # ช่องป้อนข้อความ
    st.text_input("ใส่ชื่อผู้รับพัสดุ :", on_change=on_input_change, key="user_input")

if __name__ == "__main__":
    chat()
