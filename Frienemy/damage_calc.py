import random
from Frienemy.status import hp_display
from Frienemy.damage_calc import calculate_damage

def battle(frienemy1, frienemy2):
    hp1, hp2 = frienemy1["hp"], frienemy2["hp"]
    max_hp1, max_hp2 = hp1, hp2

    print(f"⚔️ Battle Start: {frienemy1['name']} vs {frienemy2['name']} ⚔️")

    while hp1 > 0 and hp2 > 0:
        # Pick random moves for each frienemy
        move1 = random.choice(frienemy1["moves"])
        move2 = random.choice(frienemy2["moves"])

        # First frienemy attacks
        dmg1 = calculate_damage(frienemy1, move1, frienemy2)
        hp2 -= dmg1
        hp2 = max(hp2, 0)
        print(f"{frienemy1['name']} used {move1['name']}! ({dmg1} dmg)")

        if hp2 <= 0:
            break

        # Second frienemy attacks
        dmg2 = calculate_damage(frienemy2, move2, frienemy1)
        hp1 -= dmg2
        hp1 = max(hp1, 0)
        print(f"{frienemy2['name']} used {move2['name']}! ({dmg2} dmg)")

        # Show HP bars after each round
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