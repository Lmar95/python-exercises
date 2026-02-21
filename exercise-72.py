# Exercise 72 — Function that displays the cube of a number
# ─────────────────────────────────────────────────────────────────────────────

def cube(n: float) -> float:
    return n ** 3

def main():
    n = float(input("Enter a number: "))
    print(f"Cube of {n} = {cube(n)}")

if __name__ == "__main__":
    main()
