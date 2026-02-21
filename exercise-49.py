# Exercise 49 — Draw a rectangular frame of stars
# ─────────────────────────────────────────────────────────────────────────────

def draw_frame(rows: int, cols: int):
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print("*" * cols)
        else:
            print("*" + " " * (cols - 2) + "*")

def main():
    rows = int(input("Number of rows   : "))
    cols = int(input("Number of columns: "))
    draw_frame(rows, cols)

if __name__ == "__main__":
    main()
