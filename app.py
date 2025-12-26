import streamlit as st
from chatbot import chatbot_response

st.set_page_config(page_title="Simple Chatbot", page_icon="🤖")

st.title("🤖 Simple Chatbot")
st.write("Type a message and press Enter")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("You:")

if user_input:
    bot_reply = chatbot_response(user_input)

    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", bot_reply))

for speaker, message in st.session_state.chat_history:
    if speaker == "You":
        st.markdown(f"**You:** {message}")
    else:
        st.markdown(f"**Bot:** {message}")
