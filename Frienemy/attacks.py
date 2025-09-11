# Frienemy/attacks.py
import json
import os

ATTACKS_FILE = os.path.join(os.path.dirname(__file__), "attacks.json")

def load_attacks():
    with open(ATTACKS_FILE, "r") as f:
        return json.load(f)