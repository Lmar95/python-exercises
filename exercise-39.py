# Exercise 39 — Calculator (loop-based, supports multiple operations)
# ─────────────────────────────────────────────────────────────────────────────

def main():
    print("Calculator — type 'q' to quit")
    while True:
        expr = input("\nExpression (e.g. 5 + 3): ").strip()
        if expr.lower() == "q": break
        parts = expr.split()
        if len(parts) != 3:
            print("Format: number operator number"); continue
        try:
            a, op, b = float(parts[0]), parts[1], float(parts[2])
        except ValueError:
            print("Invalid numbers."); continue
        if op == "+":   print(f"= {a+b}")
        elif op == "-": print(f"= {a-b}")
        elif op == "*": print(f"= {a*b}")
        elif op == "**":print(f"= {a**b}")
        elif op in ("/","//","%"):
            if b == 0: print("Division by zero!"); continue
            print(f"= {eval(f'{a}{op}{b}')}")
        else: print(f"Unknown operator: {op}")

if __name__ == "__main__":
    main()
