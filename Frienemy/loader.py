import os
import json

def load_frienemy(name):
    """
    Load frienemy from Boxes folder (.txt JSON file).
    """
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    BOXES_PATH = os.path.join(ROOT, "Boxes")

    candidates = [
        name, name + ".txt", name + ".json",
        name.lower(), name.lower() + ".txt", name.lower() + ".json",
        name.upper(), name.upper() + ".txt", name.upper() + ".json"
    ]

    for cand in candidates:
        path = os.path.join(BOXES_PATH, cand)
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"❌ Failed to load {path}: {e}")
                return None

    print(f"⚠️ Frienemy {name} not found in Boxes/")
    return None