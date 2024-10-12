import streamlit as st

# ตั้งค่าหน้าเริ่มต้นของ Streamlit
if "current_page" not in st.session_state:
    st.session_state.current_page = "login"

# ตรวจสอบว่าเป็นหน้า login หรือไม่
if st.session_state.current_page == "login":
    ShowSidebarNavigation = false
    
def check_login():
    if "login_status" not in st.session_state:
        st.session_state.login_status = False  # กำหนดค่าเริ่มต้นเป็น False
    if not st.session_state.login_status:
        st.warning("กรุณา Login ก่อนเข้าหน้าอื่น")
        st.stop()  # หยุดการทำงานถ้าผู้ใช้ยังไม่ได้ล็อกอิน
    
def main():
    # ตรวจสอบสถานะของ current_page และเรียก switch_page ตามหน้า
   if st.session_state.current_page == "login":
        hide_sidebar()  # ซ่อน sidebar เฉพาะหน้า login
        st.switch_page("pages/1_Login.py")  # ไปที่หน้า Login
    elif st.session_state.current_page == "sign_up":
        st.switch_page("pages/2_SignUp.py")  # ไปที่หน้า Sign Up
    elif st.session_state.current_page == "home":
        st.switch_page("pages/5_Home.py")  # ไปที่หน้า Home
    elif st.session_state.current_page == "chat":
        st.switch_page("pages/4_Chatbot.py")  # ไปที่หน้า Chatbot
    elif st.session_state.current_page == "admin":
        st.switch_page("pages/3_Admin.py")  # ไปที่หน้า Admin

if __name__ == "__main__":
    main()
