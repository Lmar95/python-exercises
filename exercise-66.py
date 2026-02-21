# Exercise 66 — Triangle composed of the letter A (rows of repeated A)
# ─────────────────────────────────────────────────────────────────────────────

def main():
    n = int(input("Number of rows: "))
    for i in range(1, n + 1):
        print("A" * i)

if __name__ == "__main__":
    main()
