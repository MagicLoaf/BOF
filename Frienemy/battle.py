import os
import json
from Frienemy.status import hp_display, calculate_damage
from Frienemy.attacks import load_attacks
BOXES_PATH = os.path.join("..", "Boxes")
from Frienemy.damage_calc import calculate_damage

def fight(frienemy1, frienemy2):
    move = frienemy1["moves"][0]  # or random for CPU
    damage = calculate_damage(frienemy1, move, frienemy2)
    frienemy2["hp"] -= damage
    print(f"{frienemy1['name']} used {move['name']} and dealt {damage} damage!")
def load_frienemy(name):
    """
    Robust loader for frienemy files in BOF/Boxes.

    Tries multiple filename variants (with/without .txt/.json, underscores, case variations).
    First attempts JSON parsing; if that fails, falls back to simple "Key: Value" parsing
    (useful if you have single-line or human-readable files).
    If nothing matches, prints the files present in Boxes/ to help debugging.

    Returns: dict (frienemy data) or None on failure.
    """
    import os, json, re

    # Compute project root and Boxes path (works regardless of current working dir)
    ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    BOXES_PATH = os.path.join(ROOT, "Boxes")

    # Ensure Boxes folder exists
    if not os.path.isdir(BOXES_PATH):
        print(f"Error: Boxes folder not found at expected path: {BOXES_PATH}")
        return None

    base = name.strip()
    # Build candidate filename variants
    candidates = [
        base, base + ".txt", base + ".json",
        base.replace(" ", "_"), base.replace(" ", "_") + ".txt", base.replace(" ", "_") + ".json",
        base.lower(), base.lower() + ".txt", base.lower() + ".json",
        base.upper(), base.upper() + ".txt", base.upper() + ".json"
    ]
    # Deduplicate while keeping order
    seen = set()
    candidates = [c for c in candidates if not (c in seen or seen.add(c))]

    # Try each candidate
    for cand in candidates:
        path = os.path.join(BOXES_PATH, cand)
        if not os.path.exists(path):
            continue
        try:
            text = open(path, "r", encoding="utf-8").read()
        except Exception as e:
            print(f"Found file {path} but failed to read it: {e}")
            continue

        # Try JSON parse first
        try:
            data = json.loads(text)
            return data
        except json.JSONDecodeError:
            # Not JSON — fall back to simple "Key: Value" parsing
            try:
                obj = {}
                # Catch key:value pairs like "HP:120" or "Name: Chat_GPT" etc.
                # Also supports comma-separated moves for the 'moves' key.
                pairs = re.findall(r'([A-Za-z_ ]+):\s*([^\n]+)', text)
                for k, v in pairs:
                    key = k.strip().lower().replace(" ", "_")
                    val = v.strip()
                    # If the value looks like a list (comma separated)
                    if "," in val:
                        obj[key] = [x.strip() for x in val.split(",") if x.strip()]
                    else:
                        # try integer conversion
                        if val.isdigit():
                            obj[key] = int(val)
                        else:
                            # allow moves like TM001,TM002 without spaces
                            if key == "moves" and re.match(r'^(TM\d+(,TM\d+)*)$', val.replace(" ", "")):
                                obj[key] = [x.strip() for x in val.split(",") if x.strip()]
                            else:
                                obj[key] = val
                if obj:
                    return obj
            except Exception:
                pass

        # If file was present but couldn't parse, report it so user can inspect
        print(f"Found file {path} but could not parse it as JSON or key:value text.")

    # Nothing matched — list available files to help the user
    available = sorted(os.listdir(BOXES_PATH))
    print(f"{name} not found in Boxes/ (tried: {candidates}).")
    if available:
        print("Available files in Boxes/:")
        for a in available:
            print("  -", a)
    else:
        print("Boxes/ is empty.")
    return Nonedef battle(frienemy1, frienemy2):
    hp1, hp2 = frienemy1["hp"], frienemy2["hp"]
    max_hp1, max_hp2 = hp1, hp2

    print(f"⚔️ Battle Start: {frienemy1['name']} vs {frienemy2['name']} ⚔️")

    while hp1 > 0 and hp2 > 0:
        # Each frienemy attacks once per turn
        hp2 -= calculate_damage(frienemy1, frienemy2)
        hp1 -= calculate_damage(frienemy2, frienemy1)

        # Clamp HP to 0
        hp1 = max(hp1, 0)
        hp2 = max(hp2, 0)

        # Print HP bars
        print(f"{frienemy1['name']}: {hp_display(hp1, max_hp1)}")
        print(f"{frienemy2['name']}: {hp_display(hp2, max_hp2)}")
        print()

    # Winner
    if hp1 > 0:
        print(f"🏆 {frienemy1['name']} wins!")
    elif hp2 > 0:
        print(f"🏆 {frienemy2['name']} wins!")
    else:
        print("🤝 It's a draw!")

if __name__ == "__main__":
    f1_name = input("Enter first frienemy name: ")
    f2_name = input("Enter second frienemy name: ")

    f1 = load_frienemy(f1_name)
    f2 = load_frienemy(f2_name)

    if f1 and f2:
        battle(f1, f2)
