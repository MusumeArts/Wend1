# Bring in deps
import os
from apikey import apikey

import streamlit as st
from langchain.llms import OpenAI

os.environ['OPEN_API_KEY']= apikey

# App framework
st.title('🏳️‍⚧️ 🎹Wend1')
prompt = st.text_input('Describe Your Desired Sound')

import streamlit as st
from transformers import GPT3Tokenizer, GPT3LMHeadModel

# Load the pre-trained GPT-3 model and tokenizer
tokenizer = GPT3Tokenizer.from_pretrained('gpt3')
model = GPT3LMHeadModel.from_pretrained('gpt3')

def generate_patch(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    output = model.generate(input_ids)
    generated_patch = tokenizer.decode(output[0], skip_special_tokens=True)
    return generated_patch

# Define the Streamlit app
def app():
    st.title('Serum Patch Generator')
    
    # Collect user input
    input_text = st.text_input('Describe the patch you want:')
    
    # Generate the patch
    if input_text:
        generated_patch = generate_patch(input_text)
        st.audio(generated_patch)

# Start the app
if __name__ == '__main__':
    app()


