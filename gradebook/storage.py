import json
import os

DEFAULT_PATH = "data/gradebook.json"

def load_data(path=DEFAULT_PATH):
    try:
        with open(path,"r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "students": [],
            "courses": [],
            "enrollments": []
        }
    except json.JSONDecodeError:
        print("Error: JSON file is corrupted or invalid.")
        return {
            "students": [],
            "courses": [],
            "enrollments": []
        }
    
def save_data(data, path=DEFAULT_PATH):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error while saving data: {e}")
