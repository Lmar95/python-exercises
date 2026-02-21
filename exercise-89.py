# Exercise 89 — Display the calendar for a month
# ─────────────────────────────────────────────────────────────────────────────

import calendar

def main():
    year  = int(input("Enter the year : "))
    month = int(input("Enter the month: "))
    print()
    print(calendar.month(year, month))

if __name__ == "__main__":
    main()
