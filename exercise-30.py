# Exercise 30 — Calculate the sum of squares of the first n odd numbers
# S = 1² + 3² + 5² + ... + (2n-1)²
# ─────────────────────────────────────────────────────────────────────────────

def main():
    n = int(input("Enter N: "))
    s = sum((2*k - 1)**2 for k in range(1, n + 1))
    print(f"Sum of squares of first {n} odd numbers = {s}")

if __name__ == "__main__":
    main()
