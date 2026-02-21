# Exercise 76 — Diameter, area and perimeter functions of a circle
# ─────────────────────────────────────────────────────────────────────────────

import math

def diameter(r: float) -> float:  return 2 * r
def area(r: float) -> float:      return math.pi * r ** 2
def perimeter(r: float) -> float: return 2 * math.pi * r

def main():
    r = float(input("Enter the radius: "))
    print(f"Diameter  : {diameter(r):.4f}")
    print(f"Area      : {area(r):.4f}")
    print(f"Perimeter : {perimeter(r):.4f}")

if __name__ == "__main__":
    main()
