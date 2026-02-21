# Exercise 44 — Program that checks whether a number is perfect
# A perfect number = sum of its proper divisors (e.g. 6 = 1+2+3).
# ─────────────────────────────────────────────────────────────────────────────

def is_perfect(n: int) -> bool:
    return n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

def main():
    n = int(input("Enter a positive integer: "))
    print(f"{n} {'IS' if is_perfect(n) else 'is NOT'} a perfect number.")

if __name__ == "__main__":
    main()
