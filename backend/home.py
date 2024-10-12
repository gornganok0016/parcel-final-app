import streamlit as st

# ตั้งค่าหน้าเริ่มต้นของ Streamlit
if "current_page" not in st.session_state:
    st.session_state.current_page = "login"

# ตรวจสอบว่าเป็นหน้า login หรือไม่
if st.session_state.current_page == "login":
    ShowSidebarNavigation = false

def change_colors():
    style = """
        <style>
            body {
                background-color: #333366;  /* สีพื้นหลัง */
            }
            .stText {
                color: #2c3e50;  /* สีของตัวอักษร */
            }
            .stButton>button {
                background-color: #3498db;  /* สีพื้นหลังของปุ่ม */
                color: white;  /* สีของตัวอักษรในปุ่ม */
            }
            .stButton>button:hover {
                background-color: #2980b9;  /* สีของปุ่มเมื่อชี้เมาส์ */
            }
            footer {
                visibility: hidden;  /* ซ่อนฟุตเตอร์ */
            }
            #MainMenu {
                visibility: hidden;  /* ซ่อนเมนูหลัก */
            }
        </style>
    """
    st.markdown(style, unsafe_allow_html=True)
    
def main():
    change_colors()  # เรียกใช้ฟังก์ชันเพื่อเปลี่ยนสี
    # ตรวจสอบสถานะของ current_page และเรียก switch_page ตามหน้า
   if st.session_state.current_page == "login":
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
