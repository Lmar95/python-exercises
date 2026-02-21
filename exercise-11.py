# Exercise 11 — Program that calculates resistance in series and in parallel
# ─────────────────────────────────────────────────────────────────────────────

def resistance_series(*r) -> float:
    return sum(r)

def resistance_parallel(*r) -> float:
    return 1 / sum(1 / x for x in r)

def main():
    n  = int(input("How many resistors? "))
    rs = [float(input(f"  R{i} (Ω): ")) for i in range(1, n + 1)]
    print(f"\nSeries   : {resistance_series(*rs):.4f} Ω")
    print(f"Parallel : {resistance_parallel(*rs):.4f} Ω")

if __name__ == "__main__":
    main()
