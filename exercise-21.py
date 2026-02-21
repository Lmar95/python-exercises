# Exercise 21 — Multiple-choice conditional: if … elif … else
# Displays the season based on the month number.
# ─────────────────────────────────────────────────────────────────────────────

def main():
    m = int(input("Enter a month number (1–12): "))
    if   m in (12, 1, 2):  print("Winter")
    elif m in (3, 4, 5):   print("Spring")
    elif m in (6, 7, 8):   print("Summer")
    elif m in (9, 10, 11): print("Autumn")
    else:                   print("Invalid month number.")

if __name__ == "__main__":
    main()
