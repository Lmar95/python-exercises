# Exercise 43 — Program that calculates the GCD of two positive integers
# Uses the Euclidean algorithm.
# ─────────────────────────────────────────────────────────────────────────────

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def main():
    a = int(input("First  number: "))
    b = int(input("Second number: "))
    print(f"GCD({a}, {b}) = {gcd(a, b)}")

if __name__ == "__main__":
    main()
