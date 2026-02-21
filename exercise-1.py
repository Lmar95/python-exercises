# Exercise 1 — Program that displays the name and age of the user
# ─────────────────────────────────────────────────────────────────

def main():
    name = input("Enter your name: ")
    age  = int(input("Enter your age : "))
    print(f"\nHello, {name}! You are {age} years old.")

if __name__ == "__main__":
    main()
