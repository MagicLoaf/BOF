# status.py

def hp_display(current_hp, max_hp):
    """Return HP in [-----____] 60% style."""
    if current_hp < 0:
        current_hp = 0
    percent = int((current_hp / max_hp) * 100)

    bars = int(percent / 10)          # each bar = 10%
    line = "[" + "-" * bars + "_" * (10 - bars) + f"] {percent}% HP"

    return line
