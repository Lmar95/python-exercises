# Exercise 52 — Draw an isosceles triangle of stars (centered)
# ─────────────────────────────────────────────────────────────────────────────

def draw_isosceles(n: int):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars  = "*" * (2 * i - 1)
        print(spaces + stars)

def main():
    n = int(input("Number of rows: "))
    draw_isosceles(n)

if __name__ == "__main__":
    main()
