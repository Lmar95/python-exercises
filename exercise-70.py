# Exercise 70 — Triangle of Tifinagh alphabets
# Tifinagh Unicode block starts at U+2D30.
# ─────────────────────────────────────────────────────────────────────────────

TIFINAGH_START = 0x2D30   # ⴰ (first Tifinagh letter)
MAX_CHARS      = 33       # basic Tifinagh block has ~33 chars

def main():
    n = int(input(f"Number of rows (max {MAX_CHARS}): "))
    n = min(n, MAX_CHARS)
    for i in range(1, n + 1):
        row = " ".join(chr(TIFINAGH_START + j) for j in range(i))
        print(row)

if __name__ == "__main__":
    main()
