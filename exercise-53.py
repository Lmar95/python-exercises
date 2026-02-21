# Exercise 53 — Draw the frame (outline) of a triangle of stars
# ─────────────────────────────────────────────────────────────────────────────

def draw_triangle_frame(n: int):
    for i in range(1, n + 1):
        if i == 1:
            print(" " * (n - 1) + "*")
        elif i == n:
            print("*" * n)
        else:
            print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")

def main():
    n = int(input("Number of rows: "))
    draw_triangle_frame(n)

if __name__ == "__main__":
    main()
