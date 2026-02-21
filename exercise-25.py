# Exercise 25 — Program with the for loop
# Displays the multiplication table of a number entered by the user.
# ─────────────────────────────────────────────────────────────────────────────

def main():
    n = int(input("Enter a number: "))
    print(f"\nMultiplication table of {n}:")
    for i in range(1, 11):
        print(f"  {n} x {i:2} = {n*i:4}")

if __name__ == "__main__":
    main()
