# Exercise 7 — Program that calculates and displays the volume of a sphere
# ─────────────────────────────────────────────────────────────────────────────

import math

def sphere_volume(radius: float) -> float:
    return (4 / 3) * math.pi * radius ** 3

def main():
    radius = float(input("Enter the radius: "))
    if radius < 0:
        print("Error: radius must be positive.")
    else:
        print(f"\nVolume = {sphere_volume(radius):.4f}")

if __name__ == "__main__":
    main()
