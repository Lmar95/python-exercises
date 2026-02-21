# Exercise 47 — Draw a right-angle triangle of stars
# ─────────────────────────────────────────────────────────────────────────────

def draw_triangle(n: int):
    for i in range(1, n + 1):
        print("*" * i)

def main():
    n = int(input("Number of rows: "))
    draw_triangle(n)

if __name__ == "__main__":
    main()
