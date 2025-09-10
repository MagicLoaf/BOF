from Frienemy.status import hp_display
from Frienemy.damage_calc import calculate_damage

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