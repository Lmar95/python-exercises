# Exercise 8 — Program that exchanges the contents of two variables
# ─────────────────────────────────────────────────────────────────────────────

def main():
    a = input("Enter value for A: ")
    b = input("Enter value for B: ")
    print(f"\nBefore swap → A = {a}, B = {b}")
    a, b = b, a
    print(f"After  swap → A = {a}, B = {b}")

if __name__ == "__main__":
    main()
