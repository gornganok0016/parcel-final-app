import streamlit as st
import pandas as pd

CSV_FILE = 'backend/names.csv'  # แก้ไขให้ตรงตามพาธไฟล์

def check_question_in_csv(question):
    try:
        df = pd.read_csv(CSV_FILE)
        return question in df['name'].values
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return False

def show_chat():
    st.title("Chatbot")
    question = st.text_input("ถามคำถามของคุณที่นี่:")
    
    if st.button("ส่งคำถาม"):
        if question:
            if check_question_in_csv(question):
                answer = f"The question '{question}' is found in the CSV."
            else:
                answer = f"The question '{question}' is not found in the CSV."
        else:
            answer = "กรุณาถามคำถามที่ถูกต้อง."
        
        st.write(answer)
