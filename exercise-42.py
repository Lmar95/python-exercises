# Exercise 42 — Program that checks if a number is a palindrome
# ─────────────────────────────────────────────────────────────────────────────

def is_palindrome(n: int) -> bool:
    s = str(abs(n))
    return s == s[::-1]

def main():
    n = int(input("Enter an integer: "))
    print(f"{n} {'IS' if is_palindrome(n) else 'is NOT'} a palindrome.")

if __name__ == "__main__":
    main()
