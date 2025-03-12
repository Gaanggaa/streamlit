import json
import os
import base64

# Load Car Data from JSON
def load_car_data():
    with open("config.json", "r") as f:
        return json.load(f)["cars"]

# Convert Image to Base64 for Background
def get_base64_of_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Get AI Recommended Car Based on Budget
def get_recommended_car(budget, cars):
    for car, details in sorted(cars.items(), key=lambda x: int(x[1]["Price"].replace("$", "").replace(",", ""))):
        if int(details["Price"].replace("$", "").replace(",", "")) <= budget:
            return car
    return "No suitable car found within budget."





