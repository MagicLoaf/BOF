import os
import json

# Path to attacks.txt inside the same folder as this file
ATTACKS_FILE = os.path.join(os.path.dirname(__file__), "attacks.txt")

def load_attacks():
    """Load all attacks from attacks.txt (JSON format)."""
    if not os.path.exists(ATTACKS_FILE):
        print("⚠️ No attacks.txt found in Frienemy/. Returning empty move list.")
        return {}

    with open(ATTACKS_FILE, "r") as f:
        return json.load(f)

def get_attack(tm_code):
    """Get a single attack by TM code (e.g. 'TM001')."""
    attacks = load_attacks()
    return attacks.get(tm_code, None)
