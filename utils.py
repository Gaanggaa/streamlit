import os
import json

CONFIG_DIR = "saved_configs"

def load_configurations():
    """Loads all saved configurations."""
    configs = {}

    # Ensure the directory exists
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)  # Create the directory if missing
        return configs  # Return empty if no configurations exist

    for file in os.listdir(CONFIG_DIR):
        if file.endswith(".json"):
            file_path = os.path.join(CONFIG_DIR, file)
            try:
                with open(file_path, "r") as f:
                    config = json.load(f)
                    configs[file.replace(".json", "")] = config
            except json.JSONDecodeError:
                print(f"Error: Corrupt JSON file - {file_path}")

    return configs
