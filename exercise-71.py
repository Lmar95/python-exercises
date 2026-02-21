# Exercise 71 — Function that displays the multiplication table of a number
# ─────────────────────────────────────────────────────────────────────────────

def multiplication_table(n: int, limit: int = 10):
    print(f"Multiplication table of {n}:")
    for i in range(1, limit + 1):
        print(f"  {n} x {i:2} = {n*i:4}")

def main():
    n = int(input("Enter a number: "))
    multiplication_table(n)

if __name__ == "__main__":
    main()
