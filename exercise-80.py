# Exercise 80 — Function with an argument that takes a default value
# ─────────────────────────────────────────────────────────────────────────────

def greet(name: str, greeting: str = "Hello") -> str:
    return f"{greeting}, {name}!"

def power(base: float, exponent: float = 2) -> float:
    return base ** exponent

def main():
    # Default greeting
    print(greet("Alice"))
    print(greet("Bob", "Good morning"))

    # Default exponent (square)
    n = float(input("\nEnter a number (will be squared by default): "))
    print(f"{n}^2 = {power(n)}")
    e = float(input("Enter an exponent: "))
    print(f"{n}^{e} = {power(n, e)}")

if __name__ == "__main__":
    main()
