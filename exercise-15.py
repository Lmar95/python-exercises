# Exercise 15 — Multiple-choice conditional: if … elif … else
# Displays the month name from its number (1=January … 12=December).
# ─────────────────────────────────────────────────────────────────────────────

MONTHS = ["January","February","March","April","May","June",
          "July","August","September","October","November","December"]

def main():
    m = int(input("Enter a month number (1–12): "))
    if 1 <= m <= 12:
        print(MONTHS[m - 1])
    else:
        print("Invalid. Enter a value between 1 and 12.")

if __name__ == "__main__":
    main()
