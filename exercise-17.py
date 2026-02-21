# Exercise 17 — Program that calculates the solutions of a second-degree equation
# Solves: a·x² + b·x + c = 0
# ─────────────────────────────────────────────────────────────────────────────

import math

def solve(a, b, c):
    if a == 0:
        print("'a' must be non-zero."); return
    d = b**2 - 4*a*c
    print(f"Discriminant Δ = {d}")
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print(f"x1 = {x1:.4f},  x2 = {x2:.4f}")
    elif d == 0:
        print(f"Double root: x = {-b/(2*a):.4f}")
    else:
        r = -b/(2*a); i = math.sqrt(-d)/(2*a)
        print(f"x1 = {r:.4f}+{i:.4f}i,  x2 = {r:.4f}-{i:.4f}i")

def main():
    print("Solve: a·x² + b·x + c = 0")
    a = float(input("a: ")); b = float(input("b: ")); c = float(input("c: "))
    solve(a, b, c)

if __name__ == "__main__":
    main()
