import streamlit as st
import json
import random
import os
from PIL import Image

# Load Car Data from JSON
CONFIG_FILE = "config.json"
with open(CONFIG_FILE, "r") as f:
    cars = json.load(f)

# Page Configuration
st.set_page_config(page_title="AI Car Comparison", page_icon="🏎️", layout="wide")

# Background Styling
background_image = "background.jpg"
page_bg = f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("file://{os.getcwd()}/{background_image}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    color: white;
}}
[data-testid="stSidebar"] {{
    background-color: black;
    color: crimson;
}}
h1, h2, h3, h4, h5, h6, p, span, div {{
    font-family: 'Georgia', serif;
    color: white;
}}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Sidebar
st.sidebar.title("🚀 Explore Supercars")

# Car Selection
car1 = st.sidebar.selectbox("🏎️ Select First Car", list(cars.keys()))
car2 = st.sidebar.selectbox("🏎️ Select Second Car", list(cars.keys()))

# Display Car Details
def show_car_details(car_name):
    car_details = cars[car_name]
    image_path = f"images/{car_name.replace(' ', '_').lower()}.jpg"
    
    if os.path.exists(image_path):
        st.image(Image.open(image_path), caption=car_name, use_column_width=True)
    
    st.subheader(f"🏆 {car_name} Specifications")
    for key, value in car_details.items():
        st.write(f"**{key}:** {value}")

# Comparison Section
st.title("🏎️ AI Car Comparison")
col1, col2 = st.columns(2)
with col1:
    show_car_details(car1)
with col2:
    show_car_details(car2)

# AI-Based Recommendation
st.sidebar.subheader("🤖 Get Car Suggestions")
budget = st.sidebar.slider("💰 Set Your Budget", min_value=50000, max_value=5000000, step=50000)
recommended_cars = [name for name, details in cars.items() if int(details['Price'].strip('$').replace(',', '')) <= budget]

if st.sidebar.button("🔍 Find My Car"):
    if recommended_cars:
        selected_car = random.choice(recommended_cars)
        st.sidebar.success(f"🚗 Recommended: {selected_car}")
    else:
        st.sidebar.error("No cars available in this budget.")

# Random Car Suggestion
if st.sidebar.button("🎲 Surprise Me!"):
    random_car = random.choice(list(cars.keys()))
    st.sidebar.info(f"🔥 Check Out: {random_car}")

