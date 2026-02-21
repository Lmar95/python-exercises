# Exercise 29 — Program that calculates the factorial of a number
# ─────────────────────────────────────────────────────────────────────────────

def factorial(n: int) -> int:
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Factorial undefined for negatives.")
    else:
        print(f"{n}! = {factorial(n)}")

if __name__ == "__main__":
    main()
