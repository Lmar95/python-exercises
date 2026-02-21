# Exercise 69 — Triangle composed of alphabets in reverse order
# Row 1: A; Row 2: B A; Row 3: C B A …
# ─────────────────────────────────────────────────────────────────────────────

def main():
    n = int(input("Number of rows (max 26): "))
    for i in range(1, min(n, 26) + 1):
        print(" ".join(chr(64 + j) for j in range(i, 0, -1)))

if __name__ == "__main__":
    main()
