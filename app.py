import streamlit as st
from frontend import display_ui
from backend import handle_tasks

# Configure Streamlit Page
st.set_page_config(page_title="Streamlit Planner", page_icon="📅", layout="wide")

# Display UI
display_ui()

# Run Backend Logic
handle_tasks()
