# maker.py
import os
import json
from Frienemy.attacks import load_moves

BOXES_PATH = os.path.join("..", "Boxes")

def create_frienemy():
    # Ensure Boxes folder exists
    os.makedirs(BOXES_PATH, exist_ok=True)

    name = input("Enter frienemy name: ")
    hp = int(input("HP: "))
    attack = int(input("Attack: "))
    defense = int(input("Defense: "))
    sp_attack = int(input("Sp. Attack: "))
    sp_defense = int(input("Sp. Defense: "))
    speed = int(input("Speed: "))

    # Load available moves from moves.txt
    all_moves = load_moves()
    print("\nAvailable TMs:")
    for tm, (move_name, power) in all_moves.items():
        print(f"{tm} - {move_name} (Power {power})")

    # Let user pick up to 4 moves
    chosen_moves = []
    while len(chosen_moves) < 4:
        tm_choice = input(f"Choose TM for move slot {len(chosen_moves)+1} (or press Enter to stop): ").strip()
        if tm_choice == "":
            break
        if tm_choice in all_moves:
            chosen_moves.append(tm_choice)
            print(f"Added {all_moves[tm_choice][0]}")
        else:
            print("Invalid TM, try again.")

    frienemy = {
        "name": name,
        "hp": hp,
        "attack": attack,
        "defense": defense,
        "sp_attack": sp_attack,
        "sp_defense": sp_defense,
        "speed": speed,
        "moves": chosen_moves
    }

    file_path = os.path.join(BOXES_PATH, f"{name}.txt")
    with open(file_path, "w") as f:
        f.write(json.dumps(frienemy, indent=4))

    print(f"\n✅ {name} saved to Boxes/ with {len(chosen_moves)} moves.")

if __name__ == "__main__":
    create_frienemy()
