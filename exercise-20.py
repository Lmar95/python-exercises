# Exercise 20 — Calculator program
# ─────────────────────────────────────────────────────────────────────────────

def main():
    a  = float(input("First  number : "))
    op = input("Operator (+,-,*,/,//,%,**): ").strip()
    b  = float(input("Second number : "))

    if op == "+":   print(f"= {a + b}")
    elif op == "-": print(f"= {a - b}")
    elif op == "*": print(f"= {a * b}")
    elif op == "**":print(f"= {a ** b}")
    elif op in ("/", "//", "%"):
        if b == 0: print("Error: division by zero.")
        elif op == "/":  print(f"= {a / b}")
        elif op == "//": print(f"= {a // b}")
        else:            print(f"= {a % b}")
    else:
        print(f"Unknown operator: {op}")

if __name__ == "__main__":
    main()
