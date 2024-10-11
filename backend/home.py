import streamlit as st

def main():
    # กำหนดหน้าแรกเป็น login
    if "current_page" not in st.session_state:
        st.session_state.current_page = "login"
    
    # ตรวจสอบสถานะของ current_page และเรียก switch_page ตามหน้า
    if st.session_state.current_page == "login":
        st.switch_page("Login")  # ไปที่หน้า Login
    elif st.session_state.current_page == "sign_up":
        st.switch_page("SignUp")  # ไปที่หน้า Sign Up
    elif st.session_state.current_page == "chat":
        st.switch_page("Chatbot")  # ไปที่หน้า Sign Up
    elif st.session_state.current_page == "admin":
        st.switch_page("Admin")  # ไปที่หน้า Sign Up

if __name__ == "__main__":
    main()
