import streamlit as st
import json
import os
from PIL import Image

# Configuration directory
CONFIG_DIR = "saved_configs"
os.makedirs(CONFIG_DIR, exist_ok=True)

# Page Config
st.set_page_config(page_title="Prestige Auto Studio", page_icon="🏆", layout="wide")

# Background Image Fix
background_image = "background.jpg"  # Ensure this image exists in your project folder
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
    color: white;
}}

h1, h2, h3, h4, h5, h6, p, span, div {{
    font-family: 'Georgia', serif;
    color: white;
}}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Sidebar Title
st.sidebar.title("⚙️ Supreme Configuration Panel")

# Load Configurations Function
def load_configurations():
    configs = {}
    for file in os.listdir(CONFIG_DIR):
        if file.endswith(".json"):
            with open(os.path.join(CONFIG_DIR, file)) as f:
                configs[file.replace(".json", "")] = json.load(f)
    return configs

# Save Configurations Function
def save_configuration(name, data):
    with open(os.path.join(CONFIG_DIR, f"{name}.json"), "w") as f:
        json.dump(data, f)
    st.sidebar.success("Configuration Saved!")

# Car Options & Features
cars = {
    "Lamborghini Aventador": {"Price": "$500,000", "Horsepower": "769 HP", "Engine": "V12", "Top Speed": "217 mph", "0-60 mph": "2.8s", "Fuel Type": "Petrol"},
    "Ferrari LaFerrari": {"Price": "$1,500,000", "Horsepower": "950 HP", "Engine": "V12 Hybrid", "Top Speed": "220 mph", "0-60 mph": "2.6s", "Fuel Type": "Hybrid"},
    "Rolls-Royce Phantom": {"Price": "$450,000", "Horsepower": "563 HP", "Engine": "V12 Twin Turbo", "Top Speed": "155 mph", "0-60 mph": "5.1s", "Fuel Type": "Petrol"},
    "Bugatti Chiron": {"Price": "$3,000,000", "Horsepower": "1500 HP", "Engine": "W16 Quad Turbo", "Top Speed": "261 mph", "0-60 mph": "2.3s", "Fuel Type": "Petrol"},
    "Aston Martin Valkyrie": {"Price": "$3,200,000", "Horsepower": "1160 HP", "Engine": "V12 Hybrid", "Top Speed": "250 mph", "0-60 mph": "2.5s", "Fuel Type": "Hybrid"},
    "Porsche 911 Turbo S": {"Price": "$210,000", "Horsepower": "640 HP", "Engine": "Flat-6 Twin Turbo", "Top Speed": "205 mph", "0-60 mph": "2.6s", "Fuel Type": "Petrol"},
    "BMW M8 Competition": {"Price": "$135,000", "Horsepower": "617 HP", "Engine": "V8 Twin Turbo", "Top Speed": "190 mph", "0-60 mph": "3.0s", "Fuel Type": "Petrol"}
}

# Car Selection
selected_car = st.sidebar.selectbox("🚗 Select Your Dream Car", list(cars.keys()))
car_details = cars[selected_car]

# Car Image
car_image = f"images/{selected_car.replace(' ', '_').lower()}.jpg"  # Store car images in an 'images' folder
if os.path.exists(car_image):
    st.image(Image.open(car_image), caption=selected_car, use_column_width=True)

# Car Features Display
st.title(f"🏆 {selected_car} Configuration")
st.subheader("Specifications")
st.write(f"**Price:** {car_details['Price']}")
st.write(f"**Horsepower:** {car_details['Horsepower']}")
st.write(f"**Engine:** {car_details['Engine']}")
st.write(f"**Top Speed:** {car_details['Top Speed']}")
st.write(f"**0-60 mph:** {car_details['0-60 mph']}")
st.write(f"**Fuel Type:** {car_details['Fuel Type']}")

# Additional Customization Options
color = st.sidebar.color_picker("🎨 Select Exterior Color", "#FF0000")
rims = st.sidebar.radio("⚙️ Select Rim Type", ["Standard", "Carbon Fiber", "Sport", "Gold Plated"])
interior = st.sidebar.radio("🛋 Select Interior Finish", ["Leather", "Alcantara", "Carbon Fiber", "Diamond Stitched Leather"])
sound_system = st.sidebar.checkbox("🔊 Upgrade to Premium Sound System ($5,000)")
autopilot = st.sidebar.checkbox("🤖 Enable Autonomous Driving ($20,000)")

# Save Configuration
config_data = {
    "Car": selected_car,
    "Color": color,
    "Rims": rims,
    "Interior": interior,
    "Sound System": "Yes" if sound_system else "No",
    "Autopilot": "Yes" if autopilot else "No"
}
config_name = st.sidebar.text_input("💾 Save Configuration As")
if st.sidebar.button("💾 Save Configuration") and config_name:
    save_configuration(config_name, config_data)

# Load Saved Configurations
saved_configs = load_configurations()
if saved_configs:
    selected_config = st.sidebar.selectbox("📂 Load a Saved Configuration", saved_configs.keys())
    if st.sidebar.button("📂 Load"):
        st.session_state.update(saved_configs[selected_config])
        st.sidebar.success("Configuration Loaded!")







