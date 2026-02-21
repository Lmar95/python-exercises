# Exercise 18 — Alternative conditional structure: if … else
# Determines whether a number is positive or negative (or zero).
# ─────────────────────────────────────────────────────────────────────────────

def main():
    n = float(input("Enter a number: "))
    if n >= 0:
        print(f"{n} is positive (or zero).")
    else:
        print(f"{n} is negative.")

if __name__ == "__main__":
    main()
