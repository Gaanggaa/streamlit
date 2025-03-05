import streamlit as st
import json
import os
from PIL import Image
import time
from utils import save_configuration, load_configurations

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

# Select Car Model
car_model = st.selectbox("Select a Car Model", list(config["car_models"].keys()))

# Select Customization Options
color = st.radio("Choose a Car Color", list(config["colors"].keys()))
rim_type = st.radio("Choose Rim Type", list(config["rims"].keys()))
interior = st.radio("Choose Interior Finish", list(config["interiors"].keys()))

# Calculate Estimated Price
base_price = config["car_models"][car_model]
total_price = base_price + config["colors"][color] + config["rims"][rim_type] + config["interiors"][interior]

# Display Configurations
st.subheader("🔧 Your Configuration")
st.write(f"**Car Model:** {car_model}")
st.write(f"**Color:** {color}")
st.write(f"**Rims:** {rim_type}")
st.write(f"**Interior:** {interior}")
st.subheader(f"💰 Estimated Price: ${total_price:,}")

# Display Car Image
image_path = f"images/{car_model.lower().replace(' ', '_')}_{color.lower()}.jpg"
if os.path.exists(image_path):
    st.image(Image.open(image_path), caption=f"{car_model} in {color}", use_column_width=True)
else:
    st.warning("🚧 Image not available for this combination.")

# 3D Model (if available)
st.subheader("🚀 3D Car Model Preview")
html_code = """
<iframe width="100%" height="400px" src="https://sketchfab.com/models/your_model_id/embed"></iframe>
"""
st.components.v1.html(html_code, height=400)

# Save Configuration
if st.button("💾 Save Configuration"):
    save_configuration(car_model, color, rim_type, interior, total_price)
    st.success("Configuration saved successfully!")

# Confirmation Animation
if st.button("🚀 Confirm Configuration"):
    with st.spinner("Processing your order..."):
        time.sleep(2)
    st.balloons()
    st.success(f"Your {car_model} in {color} is ready!")


