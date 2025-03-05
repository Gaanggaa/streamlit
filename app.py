import streamlit as st
import json
import os
from PIL import Image
import time
from utils import save_configuration, load_configurationspip 

# Load car configurations
with open("config.json") as f:
    config = json.load(f)

st.set_page_config(page_title="🚗 Luxury Car Configurator", layout="wide")

# Sidebar: Load saved configurations
st.sidebar.title("🔖 Saved Configurations")
saved_configs = load_configurations()
if saved_configs:
    selected_config = st.sidebar.selectbox("Load a configuration", saved_configs.keys())
    if st.sidebar.button("Load"):
        st.session_state.update(saved_configs[selected_config])
        st.sidebar.success("Configuration Loaded!")

st.title("🚗 High-Class Car Configurator")
st.write("Customize your dream car with real-time updates and pricing.")

