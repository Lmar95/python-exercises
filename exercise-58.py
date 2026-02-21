# Exercise 58 — Create a rectangle composed of numbers
# Each row repeats its row number across all columns.
# ─────────────────────────────────────────────────────────────────────────────

def main():
    rows = int(input("Number of rows   : "))
    cols = int(input("Number of columns: "))
    for r in range(1, rows + 1):
        print(" ".join(str(r) * cols))

if __name__ == "__main__":
    main()
