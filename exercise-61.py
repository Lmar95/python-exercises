# Exercise 61 — Triangle of alternating 0s and 1s
# Row i alternates starting with i%2.
# ─────────────────────────────────────────────────────────────────────────────

def main():
    n = int(input("Number of rows: "))
    for i in range(1, n + 1):
        row = [(i + j) % 2 for j in range(i)]
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
