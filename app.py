from dotenv import load_dotenv
import os

load_dotenv()

import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Model
model = ChatMistralAI(
    model="mistral-small-2603",
    temperature=0.7
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a funny AI agent.")
    ]

st.title("🤖 Mistral AI Chatbot")

# User input
prompt = st.chat_input("Type your message...")

if prompt:
    # Show user message
    with st.chat_message("user"):
        st.write(prompt)

    # Add user message to history
    st.session_state.messages.append(HumanMessage(content=prompt))

    # Get AI response
    response = model.invoke(st.session_state.messages)

    # Add AI response to history
    st.session_state.messages.append(
        AIMessage(content=response.content)
    )

# Display chat history
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)

    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)