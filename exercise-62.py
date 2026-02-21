# Exercise 62 — Triangle composed of numbers (Pascal's-style incrementing)
# Prints a continuous sequence filling each row.
# ─────────────────────────────────────────────────────────────────────────────

def main():
    n   = int(input("Number of rows: "))
    num = 1
    for i in range(1, n + 1):
        row = []
        for _ in range(i):
            row.append(str(num))
            num += 1
        print(" ".join(row))

if __name__ == "__main__":
    main()
