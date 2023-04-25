# Bring in deps
import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI

os.environ['OPEN_API_KEY']= apikey

# App framework
st.title('🦜🔗Wend1')
prompt = st.text_input('Plug in your prompt here')