import streamlit as st

# def main():
    # st.sidebar.title("เมนู")
    # page = st.sidebar.radio("เลือกหน้า:", ["Login", "Sign Up", "หน้าแรก", "หน้าอัปโหลด", "Chatbot"])
st.title("Home Page")
st.write("ยินดีต้อนรับสู่หน้าแรกของแอปพลิเคชัน!")
if "current_page" not in st.session_state:
        st.session_state.current_page = "login"
    
    # ตรวจสอบและเปลี่ยนหน้าตามค่าของ current_page
if st.session_state.current_page == "login":
    login()
elif st.session_state.current_page == "sign_up":
    sign_up()
elif st.session_state.current_page == "home":
    home()

if __name__ == "__main__":
    main()
