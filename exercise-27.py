# Exercise 27 — Program that calculates the sum of a harmonic series
# S = 1 + 1/2 + 1/3 + ... + 1/n
# ─────────────────────────────────────────────────────────────────────────────

def main():
    n = int(input("Number of terms N: "))
    s = sum(1 / i for i in range(1, n + 1))
    print(f"Harmonic sum S(1..{n}) = {s:.6f}")

if __name__ == "__main__":
    main()
