# Exercise 36 — Program that determines whether a number is prime or not
# ─────────────────────────────────────────────────────────────────────────────

import math

def is_prime(n: int) -> bool:
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0: return False
    return True

def main():
    n = int(input("Enter an integer: "))
    print(f"{n} is {'PRIME.' if is_prime(n) else 'NOT prime.'}")

if __name__ == "__main__":
    main()
