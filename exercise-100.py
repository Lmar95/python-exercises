# Exercise 100 — Calculate the sum, average, and product of list elements
# ─────────────────────────────────────────────────────────────────────────────

from functools import reduce
import operator

def main():
    raw  = input("Enter numbers separated by spaces: ")
    data = list(map(float, raw.split()))

    total   = sum(data)
    average = total / len(data)
    product = reduce(operator.mul, data, 1)

    print(f"\nList    : {data}")
    print(f"Sum     : {total}")
    print(f"Average : {average:.4f}")
    print(f"Product : {product}")

if __name__ == "__main__":
    main()
