import os
import json

CONFIG_DIR = "saved_configs"

def save_configuration(car, color, rims, interior, price):
    """Saves the selected configuration as a JSON file."""
    if not os.path.exists(CONFIG_DIR):
        os.makedirs(CONFIG_DIR)
    
    config_data = {
        "Car": car,
        "Color": color,
        "Rims": rims,
        "Interior": interior,
        "Price": price
    }
    
    filename = f"{CONFIG_DIR}/{car.replace(' ', '_')}_{color}.json"
    with open(filename, "w") as f:
        json.dump(config_data, f)
    
def load_configurations():
    """Loads all saved configurations."""
    configs = {}
    if os.path.exists(CONFIG_DIR):
        for file in os.listdir(CONFIG_DIR):
            if file.endswith(".json"):
                with open(os.path.join(CONFIG_DIR, file)) as f:
                    config = json.load(f)
                    configs[file.replace(".json", "")] = config
    return configs
