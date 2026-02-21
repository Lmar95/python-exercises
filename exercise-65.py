# Exercise 65 — Triangle formed from a character string
# Each row prints the first i characters of the string.
# ─────────────────────────────────────────────────────────────────────────────

def main():
    s = input("Enter a string: ")
    n = len(s)
    for i in range(1, n + 1):
        print(s[:i])

if __name__ == "__main__":
    main()
