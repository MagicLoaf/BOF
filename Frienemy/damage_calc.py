import random

def calculate_damage(attacker, move, defender):
    # Check accuracy
    if random.randint(1, 100) > move["accuracy"]:
        print(f"{attacker['name']}'s {move['name']} missed!")
        return 0

    # Pick correct stat
    if move["special"] == "yes":
        atk_stat = attacker["sp_attack"]
        def_stat = defender["sp_defense"]
    else:
        atk_stat = attacker["attack"]
        def_stat = defender["defense"]

    # Simple damage formula
    damage = (atk_stat / def_stat) * move["power"]

    return int(max(1, damage))  # ensure at least 1 damage