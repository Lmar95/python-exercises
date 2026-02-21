# Exercise 75 — Function that counts the number of digits in an integer
# ─────────────────────────────────────────────────────────────────────────────

def count_digits(n: int) -> int:
    return len(str(abs(n))) if n != 0 else 1

def main():
    n = int(input("Enter an integer: "))
    print(f"{n} has {count_digits(n)} digit(s).")

if __name__ == "__main__":
    main()
