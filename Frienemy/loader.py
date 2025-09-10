import os, json, re

def load_frienemy(name):
    """
    Load a frienemy from Boxes/. Supports both JSON and simple key:value formats.
    Tries multiple filename variants to help with typos.
    """
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    BOXES_PATH = os.path.join(ROOT, "Boxes")

    if not os.path.isdir(BOXES_PATH):
        print(f"Error: Boxes folder not found at {BOXES_PATH}")
        return None

    base = name.strip()
    candidates = [
        base, base + ".txt", base + ".json",
        base.replace(" ", "_"), base.replace(" ", "_") + ".txt", base.replace(" ", "_") + ".json",
        base.lower(), base.lower() + ".txt", base.lower() + ".json",
        base.upper(), base.upper() + ".txt", base.upper() + ".json",
    ]
    seen = set()
    candidates = [c for c in candidates if not (c in seen or seen.add(c))]

    for cand in candidates:
        path = os.path.join(BOXES_PATH, cand)
        if not os.path.exists(path):
            continue
        try:
            text = open(path, "r", encoding="utf-8").read()
        except Exception as e:
            print(f"⚠️ Found {path} but failed to read: {e}")
            continue

        # JSON parse
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            # fallback parser
            obj = {}
            pairs = re.findall(r'([A-Za-z_ ]+):\s*([^\n]+)', text)
            for k, v in pairs:
                key = k.strip().lower().replace(" ", "_")
                val = v.strip()
                if "," in val:
                    obj[key] = [x.strip() for x in val.split(",") if x.strip()]
                else:
                    if val.isdigit():
                        obj[key] = int(val)
                    else:
                        obj[key] = val
            if obj:
                return obj
            print(f"⚠️ Could not parse {path}")

    print(f"{name} not found. Tried {candidates}")
    print("Files in Boxes/:", ", ".join(os.listdir(BOXES_PATH)))
    return None