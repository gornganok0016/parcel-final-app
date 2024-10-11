import streamlit as st

# def main():
    # st.sidebar.title("เมนู")
    # page = st.sidebar.radio("เลือกหน้า:", ["Login", "Sign Up", "หน้าแรก", "หน้าอัปโหลด", "Chatbot"])

    if page == "Login":
        st.switch_page("Login")  # สลับไปที่หน้า Login
    elif page == "Sign Up":
        st.switch_page("SignUp")  # สลับไปที่หน้า Sign Up
    elif page == "หน้าแรก":
        st.switch_page("Home")  # สลับไปที่หน้า Home
    elif page == "หน้าอัปโหลด":
        st.switch_page("Admin")  # สลับไปที่หน้า Admin
    elif page == "Chatbot":
        st.switch_page("Chatbot")  # สลับไปที่หน้า Chatbot

# if __name__ == "__main__":
#     main()
