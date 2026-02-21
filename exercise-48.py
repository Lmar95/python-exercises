# Exercise 48 — Draw a right-angle star triangle (inverted)
# ─────────────────────────────────────────────────────────────────────────────

def draw_triangle(n: int):
    for i in range(n, 0, -1):
        print("*" * i)

def main():
    n = int(input("Number of rows: "))
    draw_triangle(n)

if __name__ == "__main__":
    main()
