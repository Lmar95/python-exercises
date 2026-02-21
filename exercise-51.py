# Exercise 51 — Draw a diamond formed from stars
# ─────────────────────────────────────────────────────────────────────────────

def draw_diamond(n: int):
    # Upper half (including middle)
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    # Lower half
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))

def main():
    n = int(input("Half-size of diamond (rows in upper half): "))
    draw_diamond(n)

if __name__ == "__main__":
    main()
