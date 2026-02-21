# Exercise 68 — Triangle composed of alphabets (each row repeats its letter)
# Row 1: A; Row 2: B B; Row 3: C C C …
# ─────────────────────────────────────────────────────────────────────────────

def main():
    n = int(input("Number of rows (max 26): "))
    for i in range(1, min(n, 26) + 1):
        print(" ".join([chr(64 + i)] * i))

if __name__ == "__main__":
    main()
