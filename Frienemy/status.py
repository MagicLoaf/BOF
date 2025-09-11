# status.py
def hp_display(name, current_hp, max_hp):
    bar_length = 20
    filled = int(bar_length * current_hp / max_hp)
    bar = "█" * filled + "-" * (bar_length - filled)
    print(f"{name} HP: [{bar}] {current_hp}/{max_hp}")