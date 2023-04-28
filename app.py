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

# Set up OpenAI Playground Trained Model
playground_model = "Wendy"

# Initialize the prompt for generating patch parameters
# Set prompt
prompt = """(f"Generate a {input()} patch.\n\n"
          f"Oscillator 1:\n"
          f"Wavetable Position: {randint(0, 255)}\n"
          f"Unison Spread: {randint(0, 100)}\n\n"
          f"Oscillator 2:\n"
          f"Wavetable Position: {randint(0, 255)}\n"
          f"Unison Spread: {randint(0, 100)}\n\n"
          f"Mix:\n"
          f"Osc 1 Level: {randint(0, 100)}\n"
          f"Osc 2 Level: {randint(0, 100)}\n"
          f"Noise Level: {randint(0, 100)}\n\n"
          f"Filter:\n"
          f"Type: {choice(['12dB Lowpass', '24dB Lowpass', '12dB Highpass', '24dB Highpass'])}\n"
          f"Resonance: {randint(0, 100)}\n"
          f"Frequency: {randint(20, 20000)}\n\n"
          f"ADSR:\n"
          f"Attack: {uniform(0, 1):.2f}\n"
          f"Decay: {uniform(0, 1):.2f}\n"
          f"Sustain: {randint(0, 100)}\n"
          f"Release: {uniform(0, 1):.2f}\n\n"
          f"Modulation:\n"
          f"Source: {choice(['None', 'LFO', 'Envelope', 'Keyboard'])}\n"
          f"Destination: {choice(['None', 'Pitch', 'Filter', 'Volume'])}\n"
          f"Amount: {randint(0, 100)}\n\n"
          f"FX:\n"
          f"Reverb: Mix {randint(0, 100)}%, Size {randint(0, 100)}%,\n"
          f"Delay: Time {randint(0, 100)}ms, Mix {randint(0, 100)}%, Feedback {randint(0, 100)}%\n"
          f"Distortion: {choice(['Off', 'On'])}\n"
          f"Chorus: Mix {randint(0, 100)}%"
          """""
         

# App framework
st.title('🏳️‍⚧️ 🎹Wendy')
# Generate Text
prompt = st.text_input('Describe Your Desired Sound')
if prompt:
    response = openai.Completion.create(
        engine=openai_model,
        prompt=prompt,
        max_tokens=2000
    )        
    generated_text = response.choices[0].text
    # Format the generated text with bullet points
    formatted_text = "- " + generated_text.replace("\n", "\n- ")
    st.markdown(f"**Generated Patch Parameters:**\n\n{formatted_text}")
    st.write(generated_text)
    
    print(response.choices[0].text)