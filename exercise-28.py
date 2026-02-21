# Exercise 28 — Program that calculates and displays the sum of a series
# S = 1 + 1/2² + 1/3² + ... + 1/n²
# ─────────────────────────────────────────────────────────────────────────────

def main():
    n = int(input("Number of terms N: "))
    s = sum(1 / i**2 for i in range(1, n + 1))
    print(f"S = {s:.6f}")

if __name__ == "__main__":
    main()
