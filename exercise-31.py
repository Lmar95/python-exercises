# Exercise 31 — Program that calculates and displays the divisors of a number
# ─────────────────────────────────────────────────────────────────────────────

def main():
    n = int(input("Enter a positive integer: "))
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    print(f"Divisors of {n}: {divisors}")

if __name__ == "__main__":
    main()
