from Frienemy.loader import load_frienemy
from Frienemy.battle import battle

if __name__ == "__main__":
    f1_name = input("Enter first frienemy name: ")
    f2_name = input("Enter second frienemy name: ")

    f1 = load_frienemy(f1_name)
    f2 = load_frienemy(f2_name)

    if f1 and f2:
        battle(f1, f2)
    else:
        print("❌ Could not load both frienemies. Check Boxes/ folder.")