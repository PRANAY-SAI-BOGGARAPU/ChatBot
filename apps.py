import streamlit as st
import google.generativeai as genai
import os

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', 'AIzaSyCrOfry0NCFmVibCbYrEkEsyYNBIgPAARI')
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')
if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

st.set_page_config(page_title="Gemini Chat", layout="centered")
st.title("💬 My Chatbot")
st.caption("Ask me anything!I'm Ready to answer your questions.")

for msg in st.session_state.chat.history:
    role = msg.role.capitalize()
    with st.chat_message(role):
        st.markdown(msg.parts[0].text if hasattr(msg.parts[0], "text") else str(msg.parts[0]))

user_prompt = st.chat_input("Type your message here...")
if user_prompt:
    with st.chat_message("User"):
        st.markdown(user_prompt)

    try:
        response = st.session_state.chat.send_message(user_prompt)
        with st.chat_message("Gemini"):
            st.markdown(response.text)
    except Exception as e:
        st.error("An error occurred while processing your request.")
        st.exception(e)
