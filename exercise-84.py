# Exercise 84 — Program that displays the result of rolling a die
# ─────────────────────────────────────────────────────────────────────────────

import random

def roll_die(faces: int = 6) -> int:
    return random.randint(1, faces)

def main():
    rolls = int(input("How many times to roll the die? "))
    for i in range(1, rolls + 1):
        print(f"  Roll {i}: {roll_die()}")

if __name__ == "__main__":
    main()
