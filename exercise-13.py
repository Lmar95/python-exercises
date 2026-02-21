# Exercise 13 — Program that changes the contents of two variables according to a condition
# ─────────────────────────────────────────────────────────────────────────────
# Rule: A must always hold the larger value after the operation.

def main():
    a = float(input("Enter value for A: "))
    b = float(input("Enter value for B: "))
    print(f"\nBefore: A = {a}, B = {b}")
    if a < b:
        a, b = b, a
        print("Swap performed (A < B).")
    else:
        print("No swap needed.")
    print(f"After : A = {a}, B = {b}")

if __name__ == "__main__":
    main()
