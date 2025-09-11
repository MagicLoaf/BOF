import random

def calculate_damage(attacker, defender, move=None):
    """
    Very basic damage formula.
    If a move is provided, use its power.
    Otherwise, just attack - defense.
    """
    attack_stat = attacker["attack"]
    defense_stat = defender["defense"]

    if move:
        power = move.get("power", 10)
        accuracy = move.get("accuracy", 100)
        if random.randint(1, 100) > accuracy:
            return 0  # miss
        return max(1, (attack_stat * power // 50) - defense_stat)
    else:
        return max(1, attack_stat - defense_stat)