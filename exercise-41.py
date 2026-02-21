# Exercise 41 — Program that determines the inverse (reciprocal) of a number
# Also shows digit reversal of an integer.
# ─────────────────────────────────────────────────────────────────────────────

def main():
    n = float(input("Enter a number: "))
    if n == 0:
        print("Inverse of 0 is undefined.")
    else:
        print(f"Reciprocal: {1/n:.6f}")

    m = int(input("Integer to reverse digits: "))
    print(f"Reversed: {int(str(abs(m))[::-1])}")

if __name__ == "__main__":
    main()
