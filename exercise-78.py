# Exercise 78 — Function that draws a star triangle
# ─────────────────────────────────────────────────────────────────────────────

def draw_star_triangle(n: int):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2*i - 1))

def main():
    n = int(input("Number of rows: "))
    draw_star_triangle(n)

if __name__ == "__main__":
    main()
