# Exercise 16 — Program that calculates average and grade (mention) of marks
# ─────────────────────────────────────────────────────────────────────────────

def mention(avg: float) -> str:
    if   avg >= 16: return "Excellent"
    elif avg >= 14: return "Very Good"
    elif avg >= 12: return "Good"
    elif avg >= 10: return "Satisfactory"
    else:           return "Fail"

def main():
    n      = int(input("Number of subjects: "))
    grades = [float(input(f"  Grade {i}/20: ")) for i in range(1, n + 1)]
    avg    = sum(grades) / n
    print(f"\nAverage : {avg:.2f}/20  |  Mention : {mention(avg)}")

if __name__ == "__main__":
    main()
