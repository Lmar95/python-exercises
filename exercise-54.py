# Exercise 54 — Draw an isosceles triangle of stars (downward-pointing)
# ─────────────────────────────────────────────────────────────────────────────

def draw_isosceles_down(n: int):
    for i in range(n, 0, -1):
        spaces = " " * (n - i)
        stars  = "*" * (2 * i - 1)
        print(spaces + stars)

def main():
    n = int(input("Number of rows: "))
    draw_isosceles_down(n)

if __name__ == "__main__":
    main()
