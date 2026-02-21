# Exercise 55 — Draw a hollow diamond
# ─────────────────────────────────────────────────────────────────────────────

def draw_hollow_diamond(n: int):
    # Upper half
    for i in range(1, n + 1):
        if i == 1:
            print(" " * (n - 1) + "*")
        else:
            print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")
    # Lower half
    for i in range(n - 1, 0, -1):
        if i == 1:
            print(" " * (n - 1) + "*")
        else:
            print(" " * (n - i) + "*" + " " * (2 * i - 3) + "*")

def main():
    n = int(input("Half-size: "))
    draw_hollow_diamond(n)

if __name__ == "__main__":
    main()
