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

    # AI Task Priority Suggestion
def ai_task_priority(task):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You determine task priority levels."},
                  {"role": "user", "content": f"Assign a priority (Low, Medium, High) to: {task}"}],
        max_tokens=10
    )
    return response["choices"][0]["message"]["content"].strip()

    # Page Configuration
st.set_page_config(page_title="Streamlit Planner", page_icon="📅", layout="wide")
# Sidebar Navigation
st.sidebar.title("📌 Planner Features")
st.sidebar.markdown("---")
page = st.sidebar.radio("🔍 Navigate", ["📋 To-Do List", "📝 Rich Text Editor", "📌 Kanban Board", "📅 Calendar", "🤝 Collaboration", "🤖 AI Suggestions"])
st.sidebar.markdown("---")
st.sidebar.success("Select a feature to get started!")
