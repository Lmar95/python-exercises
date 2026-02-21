# Exercise 86 — Calculate the results of function calls
# Demonstrates calling multiple functions and displaying their results.
# ─────────────────────────────────────────────────────────────────────────────

import math

def square(x):     return x ** 2
def cube(x):       return x ** 3
def hypotenuse(a, b): return math.sqrt(a**2 + b**2)

def main():
    x = float(input("Enter x: "))
    print(f"square({x})     = {square(x)}")
    print(f"cube({x})       = {cube(x)}")
    a = float(input("Hypotenuse — enter a: "))
    b = float(input("Hypotenuse — enter b: "))
    print(f"hypotenuse({a},{b}) = {hypotenuse(a, b):.4f}")

if __name__ == "__main__":
    main()
