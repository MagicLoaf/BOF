from Frienemy.damage_calc import calculate_damage
from Frienemy.status import hp_display
from Frienemy.attacks import load_attacks

def battle(f1, f2):
    hp1, hp2 = f1["hp"], f2["hp"]
    max_hp1, max_hp2 = hp1, hp2
    attacks = load_attacks()

    print(f"⚔️ Battle Start: {f1['name']} vs {f2['name']} ⚔️")

    while hp1 > 0 and hp2 > 0:
        # Frienemy 1 move
        move_code1 = f1["moves"][0] if f1["moves"] else None
        move1 = attacks.get(move_code1, {}) if move_code1 else None
        dmg1 = calculate_damage(f1, f2, move1)
        hp2 = max(0, hp2 - dmg1)
        print(f"{f1['name']} used {move1['name'] if move1 else 'Attack'} → {dmg1} dmg")
        hp_display(f2["name"], hp2, max_hp2)

        if hp2 <= 0:
            print(f"🏆 {f1['name']} wins!")
            break

        # Frienemy 2 move
        move_code2 = f2["moves"][0] if f2["moves"] else None
        move2 = attacks.get(move_code2, {}) if move_code2 else None
        dmg2 = calculate_damage(f2, f1, move2)
        hp1 = max(0, hp1 - dmg2)
        print(f"{f2['name']} used {move2['name'] if move2 else 'Attack'} → {dmg2} dmg")
        hp_display(f1["name"], hp1, max_hp1)

        if hp1 <= 0:
            print(f"🏆 {f2['name']} wins!")
            break