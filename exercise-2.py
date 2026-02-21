# Exercise 2 — Program that displays a person's age from their date of birth
# ─────────────────────────────────────────────────────────────────────────────

from datetime import date

def calculate_age(birth_year: int, birth_month: int, birth_day: int) -> int:
    today      = date.today()
    birth_date = date(birth_year, birth_month, birth_day)
    age        = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

def main():
    print("Enter your date of birth:")
    year  = int(input("  Year  : "))
    month = int(input("  Month : "))
    day   = int(input("  Day   : "))
    age   = calculate_age(year, month, day)
    print(f"\nYou are {age} years old.")

if __name__ == "__main__":
    main()
