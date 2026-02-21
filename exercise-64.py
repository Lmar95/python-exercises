# Exercise 64 — Triangle composed of column indices
# Position (i, j) holds value j.
# ─────────────────────────────────────────────────────────────────────────────

def main():
    n = int(input("Number of rows: "))
    for i in range(1, n + 1):
        print(" ".join(str(j) for j in range(1, i + 1)))

if __name__ == "__main__":
    main()
