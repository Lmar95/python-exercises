# Exercise 14 — Multiple-choice conditional: if … elif … else
# Displays the day name from its number (1=Monday … 7=Sunday).
# ─────────────────────────────────────────────────────────────────────────────

def main():
    n = int(input("Enter a day number (1–7): "))
    if   n == 1: print("Monday")
    elif n == 2: print("Tuesday")
    elif n == 3: print("Wednesday")
    elif n == 4: print("Thursday")
    elif n == 5: print("Friday")
    elif n == 6: print("Saturday")
    elif n == 7: print("Sunday")
    else:        print("Invalid number. Enter a value between 1 and 7.")

if __name__ == "__main__":
    main()
