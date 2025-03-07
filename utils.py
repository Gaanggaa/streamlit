import base64
import json
import os

CONFIG_DIR = "saved_configs"
os.makedirs(CONFIG_DIR, exist_ok=True)

def get_base64_of_image(image_path):
    """Encodes an image to base64 format."""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

def load_configurations():
    """Loads saved configurations from JSON files."""
    configs = {}
    for file in os.listdir(CONFIG_DIR):
        if file.endswith(".json"):
            with open(os.path.join(CONFIG_DIR, file)) as f:
                configs[file.replace(".json", "")] = json.load(f)
    return configs

def save_configuration(name, data):
    """Saves user configurations to a JSON file."""
    with open(os.path.join(CONFIG_DIR, f"{name}.json"), "w") as f:
        json.dump(data, f)




