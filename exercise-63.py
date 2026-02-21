# Exercise 63 — Pattern composed of numbers (zigzag columns)
# Row i prints numbers from 1 to i then back from i-1 to 1.
# ─────────────────────────────────────────────────────────────────────────────

def main():
    n = int(input("Number of rows: "))
    for i in range(1, n + 1):
        row = list(range(1, i + 1)) + list(range(i - 1, 0, -1))
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
