"""\
# Exercise 3 — Program that calculates the perimeter and area of a rectangle
# ─────────────────────────────────────────────────────────────────────────────

def perimeter(length: float, width: float) -> float:
    return 2 * (length + width)

def area(length: float, width: float) -> float:
    return length * width

def main():
    length = float(input("Enter the length: "))
    width  = float(input("Enter the width : "))
    print(f"\\nPerimeter : {perimeter(length, width):.2f}")
    print(f"Area      : {area(length, width):.2f}")

if __name__ == "__main__":
    main()
"""
