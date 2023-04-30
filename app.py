# Bring in deps
import os
import streamlit as st
import openai
from apikey import apikey

os.environ['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'] = apikey
openai.api_key = apikey

from transformers import GPT2Tokenizer, GPT2LMHeadModel
tokenizer = GPT2Tokenizer.from_pretrained("microsoft/DialoGPT-large")
model = GPT2LMHeadModel.from_pretrained("microsoft/DialoGPT-large")

# Set up OpenAI Client
openai_model = 'text-davinci-002'

# Set up OpenAI Playground Trained Model
playground_model = "Wendy"

# Initialize the prompt for generating patch parameters
# Set prompt
prompt="You are an AI model named \"Wendy\", and when a user gives you a descriptive verbal input of a desired sound, you generate a list of all relevant patch parameter values for the software synthesizer \"Serum\". Do you understand?\n\nYes, I understand. I am capable of taking in verbal input from a user and generating a list of relevant patch parameter values for Serum.",

# App framework
st.title('🏳️‍⚧️ 🎹Wendy')
st.write("Please input your desired sound in the format 'Generate a [descriptor] sound'")
prompt = st.text_input('Desired Sound')
if prompt:
    # Generate Text
    prompt = f"generate a {prompt.replace('generate a ', '')} sound for the software synthesizer Serum with all relevant parameter values."
    input_ids = tokenizer.encode(prompt, return_tensors='pt')
    output = model.generate(input_ids, max_length=1024, pad_token_id=tokenizer.eos_token_id)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    # Extract and format relevant patch parameters
    patch_parameters = generated_text.split('\n')
    formatted_text = ""
    for p in patch_parameters:
        if 'Envelope' in p or 'Oscillator' in p or 'Filter' in p or 'Effects' in p or 'LFO' in p:
            formatted_text += f"- {p}\n"
    st.markdown(f"**Generated Patch Parameters:**\n\n{formatted_text}")
