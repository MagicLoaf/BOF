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
    file_path = os.path.join(BOXES_PATH, f"{name}.txt")
    if not os.path.exists(file_path):
        print(f"{name} not found in Boxes/")
        return None
    with open(file_path, "r") as f:
        return json.load(f)

def battle(frienemy1, frienemy2):
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
