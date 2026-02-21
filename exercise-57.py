# Exercise 57 — Draw a heart using stars
# ─────────────────────────────────────────────────────────────────────────────

def draw_heart(n: int = 4):
    # Upper humps
    top = ""
    for i in range(n // 2, n):
        top += " " * (n - i) + "*" * (2 * i - n) + "  " + "*" * (2 * i - n)
        top += "\n"
    # Lower triangle
    bottom = ""
    for i in range(n, 0, -1):
        bottom += " " * (n - i) + "*" * (2 * i - 1) + "\n"
    print(top + bottom)

def main():
    draw_heart()

if __name__ == "__main__":
    main()
