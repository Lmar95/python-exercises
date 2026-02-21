"""\
# Exercise 6 — Program that calculates the sum and average of grades
# ─────────────────────────────────────────────────────────────────────────────

def main():
    n      = int(input("How many grades? "))
    grades = [float(input(f"  Grade {i}: ")) for i in range(1, n + 1)]
    total  = sum(grades)
    print(f"\\nSum     : {total:.2f}")
    print(f"Average : {total / n:.2f}")

if __name__ == "__main__":
    main()
"""
