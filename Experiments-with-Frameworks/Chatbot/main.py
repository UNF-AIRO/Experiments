# Import frameworks
import pickle
import chatbot as cb
from keras.models import load_model

import json
import random
import nltk
import streamlit as st
from pydantic import BaseModel
from typing import List
# Downloads needed nltk
nltk.download('punkt')
nltk.download('wordnet')

# Loads needed files
model = load_model('chatbot_model.h5')
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))
oldMessage = "hi!"



# Message class defined in Pydantic
class Message(BaseModel):
    isAi: bool
    text: str

# Sets page config for the streamlit page
st.set_page_config(page_title='AiRO', page_icon='🧠', layout="wide")

def local_css():
   with open("style.css") as f:
       # Customizes the CSS
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# Loads Custom CSS
local_css()

# Intializes the state variables (the vars that are persistant)
if 'count' not in st.session_state:
	st.session_state.count = 0

if 'messages' not in st.session_state:
	st.session_state.messages = list()

if 'newMessage' not in st.session_state:
	st.session_state.newMessage = ""

def chatBubble(message):
    # Initalize columns so the messages are at opposite sides of the page
    col1, col2 = st.columns(2)
    if message.isAi:
         with col1:
            # Html bubble message
            st.markdown(f'<div class="chat"><div class="yours messages"><div class="message last">{message.text}</div></div> <div class="yours messages">', unsafe_allow_html=True)
    else:
         with col2:
             # Html bubble message
            st.markdown(f'<div class="chat"><div class="mine messages"><div class="message last">{message.text}</div></div> <div class="mine messages">', unsafe_allow_html=True)
# Image on top
st.image("AiRO.png")

# Title below image
st.title("Artificial Intelligence Research Organization")

# Subheader below title
st.subheader("Chat about UNF...")

# Initalize button
start = st.button("Chat")

# If start then add to count state var, is a count so that when the page updates, the chat still appears
if start:
    st.session_state.count += 1
if  st.session_state.count > 0:
        st.session_state.messages.append(Message(isAi=False, text= st.session_state.newMessage))
        aiMessage = Message(isAi=True, text=cb.chatbot_response(st.session_state.newMessage))
        st.session_state.messages.append(aiMessage)
        #chatBubble(st.session_state.lastMessage)
        for message in st.session_state.messages:
            chatBubble(message)
        
       
        
        
        
    # Set newMessage to a text field
        #st.session_state.newMessage = st.text_input("Send Message")
        st.text_input("Send Message", key="newMessage")
       

    # Initalize button
   

    # If send, send the message and process the text for the chatbot
    

    # Display the chat bubbles
     
       
    
