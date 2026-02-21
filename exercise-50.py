# Exercise 50 — Draw a square frame of stars (n×n)
# ─────────────────────────────────────────────────────────────────────────────

def draw_square_frame(n: int):
    for i in range(n):
        if i == 0 or i == n - 1:
            print("*" * n)
        else:
            print("*" + " " * (n - 2) + "*")

def main():
    n = int(input("Frame size (n×n): "))
    draw_square_frame(n)

if __name__ == "__main__":
    main()
