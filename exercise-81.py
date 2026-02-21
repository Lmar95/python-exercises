# Exercise 81 — Result of calculating a function
# Demonstrates defining and evaluating a mathematical function f(x).
# ─────────────────────────────────────────────────────────────────────────────

def f(x: float) -> float:
    """f(x) = 3x² - 2x + 1"""
    return 3*x**2 - 2*x + 1

def g(x: float) -> float:
    """g(x) = (x + 1) / (x - 1)  — undefined for x=1"""
    if x == 1:
        raise ValueError("g(x) is undefined for x = 1")
    return (x + 1) / (x - 1)

def main():
    x = float(input("Enter x: "))
    print(f"f({x}) = {f(x):.4f}")
    try:
        print(f"g({x}) = {g(x):.4f}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
