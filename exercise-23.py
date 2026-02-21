# Exercise 23 — Program that checks whether a year is a leap year or not
# ─────────────────────────────────────────────────────────────────────────────

def is_leap(y: int) -> bool:
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

def main():
    y = int(input("Enter a year: "))
    print(f"{y} is {'a LEAP year.' if is_leap(y) else 'NOT a leap year.'}")

if __name__ == "__main__":
    main()
