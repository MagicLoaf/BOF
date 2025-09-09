# status.py
def hp_display(current_hp, max_hp):
    percentage = int((current_hp / max_hp) * 100)
    filled = "-" * (percentage // 10)
    empty = "_" * (10 - (percentage // 10))
    return f"[{filled}{empty}] {percentage}% HP"

def calculate_damage(attacker, defender, move_power):
    return max(1, (attacker["attack"] - defender["defense"]) + move_power)
    return line
