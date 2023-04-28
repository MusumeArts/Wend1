# Bring in deps
import os
import streamlit as st
import openai
from apikey import apikey

os.environ['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']= apikey
openai.api_key = apikey

from langchain.llms import OpenAI
from transformers import GPT2Tokenizer, GPT2LMHeadModel
# Set up OpenAPI key

# Set up OpenAI Client
openai_model = 'text-davinci-003'

# App framework
st.title('🏳️‍⚧️ 🎹Wend1')
# Generate Text
prompt = st.text_input('Describe Your Desired Sound')
if prompt:
    response = openai.Completion.create(
        engine=openai_model,
        prompt=prompt,
        max_tokens=50
    )        
    generated_text = response.choices[0].text
    st.write(generated_text)
    
    print(response.choices[0].text)