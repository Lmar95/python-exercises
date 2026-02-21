# Exercise 22 — Program that checks if a number is even or odd
# ─────────────────────────────────────────────────────────────────────────────

def main():
    n = int(input("Enter an integer: "))
    print("EVEN." if n % 2 == 0 else "ODD.")

if __name__ == "__main__":
    main()
