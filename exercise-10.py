# Exercise 10 — Program that calculates the distance between two points A and B
# ─────────────────────────────────────────────────────────────────────────────

import math

def distance(x1, y1, x2, y2) -> float:
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def main():
    print("Point A:")
    x1, y1 = float(input("  x: ")), float(input("  y: "))
    print("Point B:")
    x2, y2 = float(input("  x: ")), float(input("  y: "))
    print(f"\nDistance AB = {distance(x1, y1, x2, y2):.4f}")

if __name__ == "__main__":
    main()
