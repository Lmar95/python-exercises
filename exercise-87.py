# Exercise 87 — Create and import a module containing statistical functions
# All statistical functions are defined here and used in main().
# ─────────────────────────────────────────────────────────────────────────────

def mean(data: list) -> float:
    return sum(data) / len(data)

def variance(data: list) -> float:
    m = mean(data)
    return sum((x - m)**2 for x in data) / len(data)

def std_dev(data: list) -> float:
    import math
    return math.sqrt(variance(data))

def median(data: list) -> float:
    s = sorted(data)
    n = len(s)
    return s[n//2] if n % 2 != 0 else (s[n//2 - 1] + s[n//2]) / 2

def main():
    raw  = input("Enter numbers separated by spaces: ")
    data = list(map(float, raw.split()))
    print(f"Mean     : {mean(data):.4f}")
    print(f"Median   : {median(data):.4f}")
    print(f"Variance : {variance(data):.4f}")
    print(f"Std Dev  : {std_dev(data):.4f}")

if __name__ == "__main__":
    main()
