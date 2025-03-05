import os
import json

CONFIG_DIR = "saved_configs"
os.makedirs(CONFIG_DIR, exist_ok=True)  # Ensure the folder exists

def load_configurations():
    """Loads all saved configurations from JSON files."""
    configs = {}
    for file in os.listdir(CONFIG_DIR):
        if file.endswith(".json"):
            file_path = os.path.join(CONFIG_DIR, file)
            try:
                with open(file_path, "r") as f:
                    config = json.load(f)
                    configs[file.replace(".json", "")] = config
            except json.JSONDecodeError:
                print(f"⚠️ Warning: Corrupt JSON file - {file}")
    return configs

def save_configuration(name, data):
    """Saves a car configuration to a JSON file."""
    file_path = os.path.join(CONFIG_DIR, f"{name}.json")
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)  # Pretty format for readability

