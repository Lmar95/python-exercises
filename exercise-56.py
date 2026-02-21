# Exercise 56 — Draw the letter A using stars
# ─────────────────────────────────────────────────────────────────────────────

def draw_letter_A():
    pattern = [
        "  *  ",
        " * * ",
        "*   *",
        "*****",
        "*   *",
        "*   *",
    ]
    for line in pattern:
        print(line)

def main():
    draw_letter_A()

if __name__ == "__main__":
    main()
