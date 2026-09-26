# app/storage.py
import json
import os

filename = "contacts.json"

def get_contacts():
    if os.path.exists(filename):
        try:
            with open(filename, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_all_contacts(data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)