import streamlit as st
import pandas as pd
import datetime
from streamlit_lottie import st_lottie
import json
import openai
import os
from dotenv import load_dotenv 

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

#Lottie animation
@st.cache_data
def load_lottie(filepath):
    with open(filepath, "r") as f:
        return json.load(f)
    
# AI Task Suggestion
def ai_suggest_task(context):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a productivity assistant."},
                  {"role": "user", "content": f"Suggest a task based on: {context}"}],
        max_tokens=50
    )
    return response["choices"][0]["message"]["content"].strip()