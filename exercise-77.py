# Exercise 77 — Program that calculates solutions of a second-degree equation
# (using functions — same logic as Ex.17 but structured with dedicated functions)
# ─────────────────────────────────────────────────────────────────────────────

import math

def discriminant(a: float, b: float, c: float) -> float:
    return b**2 - 4*a*c

def solve(a: float, b: float, c: float):
    d = discriminant(a, b, c)
    if d > 0:
        return (-b + math.sqrt(d))/(2*a), (-b - math.sqrt(d))/(2*a)
    elif d == 0:
        return (-b/(2*a),)
    else:
        r = -b/(2*a); i = math.sqrt(-d)/(2*a)
        return (complex(r, i), complex(r, -i))

def main():
    a = float(input("a: ")); b = float(input("b: ")); c = float(input("c: "))
    roots = solve(a, b, c)
    print("Roots:", roots)

if __name__ == "__main__":
    main()
