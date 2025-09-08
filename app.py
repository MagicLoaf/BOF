import sys, os
sys.path.append(os.path.dirname(__file__))  # makes BOF root visible

import os
from FrienemiesMaker import maker
from Frienemy import battle

def main():
    print("1. Create Frienemy")
    print("2. Battle")
    choice = input("Choose an option: ")

    if choice == "1":
        maker.create_frienemy()
    elif choice == "2":
        # run battle.py logic
        f1 = input("Enter first frienemy name: ")
        f2 = input("Enter second frienemy name: ")
        fr1 = battle.load_frienemy(f1)
        fr2 = battle.load_frienemy(f2)
        if fr1 and fr2:
            battle.battle(fr1, fr2)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
