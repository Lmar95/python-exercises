"""\
# Exercise 12 — Program that returns whether two numbers have the same sign
# ─────────────────────────────────────────────────────────────────────────────

def same_sign(a: float, b: float) -> bool:
    return (a >= 0 and b >= 0) or (a < 0 and b < 0)

def main():
    a = float(input("First  number: "))
    b = float(input("Second number: "))
    if same_sign(a, b):
        print(f"\\n{a} and {b} have the SAME sign.")
    else:
        print(f"\\n{a} and {b} have DIFFERENT signs.")

if __name__ == "__main__":
    main()
"""
