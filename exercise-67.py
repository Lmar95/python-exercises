# Exercise 67 — Triangle composed of sequential alphabets (A, B, C …)
# Row 1: A; Row 2: A B; Row 3: A B C …
# ─────────────────────────────────────────────────────────────────────────────

def main():
    n = int(input("Number of rows (max 26): "))
    for i in range(1, min(n, 26) + 1):
        print(" ".join(chr(65 + j) for j in range(i)))

if __name__ == "__main__":
    main()
