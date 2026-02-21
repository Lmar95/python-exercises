# Exercise 45 — Rock, Paper, Scissors game
# ─────────────────────────────────────────────────────────────────────────────

import random

CHOICES      = ["rock", "paper", "scissors"]
WINS_AGAINST = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

def main():
    rounds = int(input("How many rounds? "))
    player_score = computer_score = 0

    for r in range(1, rounds + 1):
        player   = input(f"Round {r} — rock/paper/scissors: ").strip().lower()
        if player not in CHOICES:
            print("Invalid choice, round skipped."); continue
        computer = random.choice(CHOICES)
        print(f"Computer: {computer}")
        if player == computer:
            print("Tie!")
        elif WINS_AGAINST[player] == computer:
            print("You win!"); player_score += 1
        else:
            print("Computer wins!"); computer_score += 1

    print(f"\nFinal — You: {player_score}  Computer: {computer_score}")

if __name__ == "__main__":
    main()
