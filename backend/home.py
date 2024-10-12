import streamlit as st

def main():
    # กำหนดหน้าแรกเป็น login
    if "current_page" not in st.session_state:
        st.session_state.current_page = "login"
    
    # ตรวจสอบสถานะของ current_page และซ่อน sidebar สำหรับหน้า login
    if st.session_state.current_page == "login":
        # ซ่อน sidebar ในหน้า login
        st.set_page_config(layout="centered")  # ซ่อน sidebar
        st.switch_page("pages/1_Login.py")  # ไปที่หน้า Login
    elif st.session_state.current_page == "login for admin":
        st.switch_page("pages/6_Login_admin.py")  # ไปที่หน้า Login
    elif st.session_state.current_page == "sign_up":
        st.switch_page("pages/2_SignUp.py")  # ไปที่หน้า Sign Up
    elif st.session_state.current_page == "home":
        # แสดง sidebar ตามปกติในหน้าอื่น
        st.set_page_config(layout="wide")  # แสดง sidebar ในหน้าอื่น
        st.switch_page("pages/5_Home.py")  # ไปที่หน้า Home
    elif st.session_state.current_page == "chat":
        st.switch_page("pages/4_Chatbot.py")  # ไปที่หน้า Chatbot
    elif st.session_state.current_page == "admin":
        st.switch_page("pages/3_Admin.py")  # ไปที่หน้า Admin
        
if __name__ == "__main__":
    main()
