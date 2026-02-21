# Exercise 37 — Nested for loops: full multiplication table
# ─────────────────────────────────────────────────────────────────────────────

def main():
    n = int(input("Table size (e.g. 10): "))
    header = "     " + "".join(f"{c:5}" for c in range(1, n+1))
    print(header)
    print("-" * len(header))
    for r in range(1, n+1):
        row = f"{r:4} |" + "".join(f"{r*c:5}" for c in range(1, n+1))
        print(row)

if __name__ == "__main__":
    main()
