# Frienemy/attacks.py
import os
import json

THIS_DIR = os.path.dirname(__file__)
ATTACKS_FILE = os.path.join(THIS_DIR, "attacks.txt")

def _parse_csv_line(line):
    # Accept either: TM001,Name,Power,Type,Special,Accuracy
    # or: TM001,Name,Power
    parts = [p.strip() for p in line.split(",")]
    if len(parts) < 3:
        return None
    tm = parts[0]
    name = parts[1]
    try:
        power = int(parts[2])
    except ValueError:
        power = 0
    # optional fields
    move_type = parts[3] if len(parts) >= 4 else None
    special = parts[4].lower() if len(parts) >= 5 else "no"
    # normalize special to "yes"/"no"
    special = "yes" if special in ("yes", "y", "true", "1") else "no"
    try:
        accuracy = int(parts[5]) if len(parts) >= 6 and parts[5] != "" else 100
    except ValueError:
        accuracy = 100

    return tm, {
        "name": name,
        "power": power,
        "type": move_type,
        "special": special,
        "accuracy": accuracy
    }

def load_attacks():
    """
    Load attacks from attacks.txt. Supports JSON (dict) or CSV lines.
    Returns dict keyed by TM code: { "TM001": {"name":..,"power":..,"type":..,"special":..,"accuracy":..}, ...}
    """
    if not os.path.exists(ATTACKS_FILE):
        print("⚠️ attacks.txt not found in Frienemy/ - returning empty dict")
        return {}

    text = open(ATTACKS_FILE, "r", encoding="utf-8").read().strip()
    if not text:
        return {}

    # Try JSON first
    try:
        data = json.loads(text)
        # If it's a list, convert to dict assuming entries contain 'code'
        if isinstance(data, list):
            out = {}
            for item in data:
                if isinstance(item, dict) and "code" in item:
                    code = item["code"]
                    out[code] = {
                        "name": item.get("name",""),
                        "power": int(item.get("power",0)),
                        "type": item.get("type"),
                        "special": "yes" if str(item.get("special","no")).lower() in ("yes","y","true","1") else "no",
                        "accuracy": int(item.get("accuracy",100))
                    }
            return out
        elif isinstance(data, dict):
            # Ensure normalization of values
            out = {}
            for k, v in data.items():
                if isinstance(v, dict):
                    out[k] = {
                        "name": v.get("name",""),
                        "power": int(v.get("power",0)),
                        "type": v.get("type"),
                        "special": "yes" if str(v.get("special","no")).lower() in ("yes","y","true","1") else "no",
                        "accuracy": int(v.get("accuracy",100))
                    }
            return out
    except Exception:
        # Not JSON -> parse as CSV-style file
        pass

    out = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        parsed = _parse_csv_line(line)
        if parsed:
            tm, info = parsed
            out[tm] = info
        else:
            print(f"⚠️ Could not parse line in attacks.txt: {line}")

    return out

# convenience wrappers
def get_attack(tm_code):
    atks = load_attacks()
    return atks.get(tm_code)

# compatibility alias
load_moves = load_attacks