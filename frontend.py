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