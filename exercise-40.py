# Exercise 40 — Program that counts the number of digits in an integer
# ─────────────────────────────────────────────────────────────────────────────

def count_digits(n: int) -> int:
    n = abs(n)
    if n == 0: return 1
    count = 0
    while n:
        count += 1; n //= 10
    return count

def main():
    n = int(input("Enter an integer: "))
    print(f"{n} has {count_digits(n)} digit(s).")

if __name__ == "__main__":
    main()
