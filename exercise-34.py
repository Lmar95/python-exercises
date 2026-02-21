# Exercise 34 — Sum of alternating series S = 1 - 1/2 + 1/3 - 1/4 + ...
# ─────────────────────────────────────────────────────────────────────────────

def main():
    n = int(input("Number of terms N: "))
    s = sum((-1)**(i+1) / i for i in range(1, n + 1))
    print(f"S ({n} terms) = {s:.6f}  (converges to ln(2) ≈ 0.693147)")

if __name__ == "__main__":
    main()
