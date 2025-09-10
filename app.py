import sys
from Frienemy.loader import load_frienemy
from Frienemy.battle import battle
from FrienemiesMaker import maker  # optional: to create frienemies from menu

def main():
    print("=== BOF Battle Simulator ===")
    print("1. Create a new frienemy")
    print("2. Start a battle")
    print("3. Quit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        maker.create_frienemy()

    elif choice == "2":
        f1_name = input("Enter first frienemy name: ")
        f2_name = input("Enter second frienemy name: ")

        f1 = load_frienemy(f1_name)
        f2 = load_frienemy(f2_name)

        if f1 and f2:
            battle(f1, f2)
        else:
            print("⚠️ One or both frienemies could not be loaded.")

    elif choice == "3":
        print("👋 Exiting.")
        sys.exit(0)

    else:
        print("❌ Invalid choice.")

if __name__ == "__main__":
    main()
