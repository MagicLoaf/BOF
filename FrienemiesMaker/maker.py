# maker.py
from Frienemy.attacks import load_attacks
import os, json, math

BOXES_PATH = os.path.join("..", "Boxes")
os.makedirs(BOXES_PATH, exist_ok=True)

def create_frienemy():
    attacks = load_attacks()  # dictionary of all moves
    tm_codes = list(attacks.keys())  # keep order
    moves_per_page = 4
    current_page = 0

    name = input("Enter frienemy name: ")
    hp = int(input("HP: "))
    attack = int(input("Attack: "))
    defense = int(input("Defense: "))
    sp_attack = int(input("Sp. Attack: "))
    sp_defense = int(input("Sp. Defense: "))
    speed = int(input("Speed: "))

    chosen_moves = []

    # pick up to 4 moves
    while len(chosen_moves) < 4:
        start = current_page * moves_per_page
        end = start + moves_per_page
        page_moves = tm_codes[start:end]

        print("\nAvailable TMs (Page", current_page + 1, "/", math.ceil(len(tm_codes)/moves_per_page), "):")
        for i, code in enumerate(page_moves, 1):
            move = attacks[code]
            print(f"{i}. {code} - {move['name']} (Power {move['power']})")

        print("\nOptions: [1-4] pick move | D = next page | A = previous page | Enter = finish")

        choice = input("Choose: ").strip().upper()

        if choice in ["1","2","3","4"]:
            idx = int(choice) - 1
            if idx < len(page_moves):
                tm_code = page_moves[idx]
                if tm_code not in chosen_moves:
                    chosen_moves.append(tm_code)
                    print(f"Added {attacks[tm_code]['name']}!")
                else:
                    print("Already chosen.")
        elif choice == "D":
            if end < len(tm_codes):
                current_page += 1
            else:
                print("⚠️ Already on last page.")
        elif choice == "A":
            if current_page > 0:
                current_page -= 1
            else:
                print("⚠️ Already on first page.")
        elif choice == "":
            break
        else:
            print("Invalid input.")

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

    # ----- SAFE SAVE (updated block) -----
    # sanitize filename (simple)
    safe_name = name.strip().replace(" ", "_")
    file_path = os.path.join(BOXES_PATH, f"{safe_name}.txt")

    try:
        # ensure Boxes folder exists (redundant but safe)
        os.makedirs(BOXES_PATH, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(frienemy, f, indent=4)

        abs_path = os.path.abspath(file_path)
        print(f"\n✅ {name} saved to Boxes/ with moves: {', '.join(chosen_moves)}")
        print(f"Location: {abs_path}")
    except Exception as e:
        print(f"\n❌ Failed to save frienemy {name}: {e}")