import streamlit as st
import pandas as pd

st.markdown("""
 <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
            width: 100vw;
            height: 100vh;
            overflow: hidden;
        }
        
        .container {
            width: 100vw;
            height: 100vh;
            max-width: none;
            margin: 0 auto;
            background-color: #ffe5e5;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        
        .chat-header {
            background-color: #ff6f6f;
            padding: 19px;
            text-align: center;
            color: white;
            font-weight: bold;
            position: relative;
            /* ทำให้สามารถจัดตำแหน่งปุ่มใน header ได้ */
        }
        
        .back-button {
            position: absolute;
            left: 15px;
            /* กำหนดตำแหน่งอยู่ทางซ้าย */
            top: 50%;
            transform: translateY(-50%);
            /* จัดให้ปุ่มอยู่กลางแนวตั้ง */
            background: none;
            border: none;
            color: white;
            font-size: 18px;
            /* ขนาดของปุ่ม */
            cursor: pointer;
        }
        
        .chat-container {
            flex-grow: 1;
            padding: 25px;
            overflow-y: auto;
            word-wrap: break-word;
        }
        
        .message {
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }
        
        .message.user {
            justify-content: flex-end;
        }
        
        .message.user .message-text {
            order: 1;
        }
        
        .message.user img {
            order: 2;
            margin-left: 10px;
        }
        
        .message.bot {
            justify-content: flex-start;
        }
        
        .message-text {
            padding: 10px;
            border-radius: 20px;
            max-width: 70%;
            font-size: 14px;
        }
        
        .message.user .message-text {
            background-color: #b2ebf2;
            color: black;
        }
        
        .message.bot .message-text {
            background-color: #f0f0f0;
            color: black;
        }
        
        .message img {
            width: 30px;
            height: 30px;
            border-radius: 50%;
        }
        
        .chat-footer {
            display: flex;
            align-items: center;
            padding: 10px;
            background-color: white;
            border-top: 1px solid #ddd;
        }
        
        .input-text {
            flex-grow: 1;
            padding: 10px;
            border-radius: 20px;
            border: 1px solid #ddd;
            outline: none;
        }
        
        .send-button {
            background-color: #ff6f6f;
            color: white;
            border: none;
            border-radius: 20px;
            padding: 10px;
            margin-left: 10px;
            cursor: pointer;
        }
        
        .send-button:hover {
            background-color: #ff4f4f;
        }
        
        .loading {
            display: none;
            text-align: center;
            color: #ff6f6f;
        }
        
        @media (max-width: 768px) {
            .container {
                height: 100vh;
                width: 100%;
                padding: 0;
            }
            .message-text {
                max-width: 85%;
                font-size: 12px;
            }
            .send-button {
                padding: 8px;
                font-size: 12px;
            }
            .input-text {
                padding: 8px;
                font-size: 14px;
            }
            .message img {
                width: 25px;
                height: 25px;
            }
        }
        
        @media (min-width: 769px) and (max-width: 1200px) {
            .container {
                height: 100vh;
                width: 90%;
            }
            .message-text {
                max-width: 80%;
                font-size: 14px;
            }
            .send-button {
                padding: 10px;
                font-size: 14px;
            }
            .input-text {
                padding: 10px;
                font-size: 16px;
            }
        }
    </style>
""", unsafe_allow_html=True)

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
