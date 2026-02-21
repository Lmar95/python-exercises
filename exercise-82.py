# Exercise 82 — Functions cos(), sin() and pi
# ─────────────────────────────────────────────────────────────────────────────

import math

def main():
    print(f"π  = {math.pi:.6f}")

    angle_deg = float(input("Enter an angle in degrees: "))
    angle_rad = math.radians(angle_deg)

    print(f"sin({angle_deg}°) = {math.sin(angle_rad):.6f}")
    print(f"cos({angle_deg}°) = {math.cos(angle_rad):.6f}")
    print(f"tan({angle_deg}°) = {math.tan(angle_rad):.6f}")

if __name__ == "__main__":
    main()
