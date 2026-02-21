# Exercise 59 — Create a right-angle triangle composed of numbers
# Row i contains the number i repeated i times.
# ─────────────────────────────────────────────────────────────────────────────

def main():
    n = int(input("Number of rows: "))
    for i in range(1, n + 1):
        print(" ".join([str(i)] * i))

if __name__ == "__main__":
    main()
