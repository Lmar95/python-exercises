# Exercise 5 — Operations Program: Sum, Product, Subtraction and Division
# ─────────────────────────────────────────────────────────────────────────────

def main():
    a = float(input("Enter the first  number: "))
    b = float(input("Enter the second number: "))
    print(f"\nSum        : {a + b}")
    print(f"Subtraction: {a - b}")
    print(f"Product    : {a * b}")
    if b != 0:
        print(f"Division   : {a / b:.4f}")
    else:
        print("Division   : undefined (division by zero)")

if __name__ == "__main__":
    main()
