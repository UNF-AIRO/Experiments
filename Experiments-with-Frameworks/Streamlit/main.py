import streamlit as st
from pydantic import BaseModel
from typing import List
import os
# Message class defined in Pydantic
class Message(BaseModel):
    isAi: bool
    text: str

message = Message(isAi=False, text= "")
st.set_page_config(page_title='AiRO', page_icon='🧠', layout="wide")

def local_css():
   with open("style.css") as f:
    
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css()

if 'count' not in st.session_state:
	st.session_state.count = 0

if 'messages' not in st.session_state:
	st.session_state.messages = list()

def chatBubble(message):
    col1, col2, col3 = st.columns(3)
    if message.isAi:
        with col1:
            st.markdown(f'<div class="chat"><div class="yours messages"><div class="message last">{message.text}</div></div> <div class="yours messages">', unsafe_allow_html=True)
    else:
        with col2:
            st.markdown(f'<div class="chat"><div class="mine messages"><div class="message last">{message.text}</div></div> <div class="mine messages">', unsafe_allow_html=True)

st.image("AiRO.png")
st.title("Artificial Intelligence Research Organization")

st.subheader("Chat about UNF...")

start = st.button("Chat")

if start:
    st.session_state.count += 1
if  st.session_state.count > 0:
    
    newMessage = st.text_input("Send Message")
    send = st.button("Send")
    if send:
        message = Message(isAi=False, text= newMessage)
        st.session_state.messages.insert(0, message)

    for message in st.session_state.messages:
        chatBubble(message)
        chatBubble(Message(isAi=True, text="Hello!"))
