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

