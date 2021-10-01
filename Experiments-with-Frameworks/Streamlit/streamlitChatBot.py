import streamlit as st
from pydantic import BaseModel
from typing import List

# Message class defined in Pydantic
class Message(BaseModel):
    isAi: bool
    text: str

st.set_page_config(page_title='AiRO', page_icon='./AiRO.png')

def local_css(file_name):
    f = open(file_name,)
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")
if 'count' not in st.session_state:
	st.session_state.count = 0

if 'messages' not in st.session_state:
	st.session_state.messages = []
    
def chatBubble(message):
    col1, col2, col3 = st.columns(3)
    if message.isAi:
        with col1:
            st.markdown(f'<div class="chat"><div class="yours messages"><div class="message last">{message.text}</div></div> <div class="yours messages">', unsafe_allow_html=True)
    else:
        with col2:
                  st.markdown(f'<div class="chat"><div class="mine messages"><div class="message last">{message.text}</div></div> <div class="mine messages">', unsafe_allow_html=True)

st.image("AiRO.png")
st.title(" Artificial Intelligence Research Organization")

st.subheader("Chat about UNF...")

start = st.button("Chat")

if start:
    st.session_state.count += 1
if  st.session_state.count > 0:
    for message in st.session_state.messages:
        chatBubble(message)
        chatBubble(Message(isAi=True, text="Hello!"))
    newMessage = st.text_input("Send Message")
    send = st.button("Send")
    if send:
        st.session_state.messages.append(Message(isAi=False, text= newMessage))
        

    

