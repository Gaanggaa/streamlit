import json
import os

CONFIG_DIR = "saved_configs"
os.makedirs(CONFIG_DIR, exist_ok=True)

def load_configurations():
    """Loads all saved car configurations from JSON files."""
    configs = {}
    for file in os.listdir(CONFIG_DIR):
        if file.endswith(".json"):
            with open(os.path.join(CONFIG_DIR, file)) as f:
                configs[file.replace(".json", "")] = json.load(f)
    return configs

def save_configuration(name, data):
    """Saves a car configuration as a JSON file."""
    with open(os.path.join(CONFIG_DIR, f"{name}.json"), "w") as f:
        json.dump(data, f, indent=4)
    return "Configuration Saved Successfully!"


