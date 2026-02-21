# Exercise 32 — The for loop (various demonstrations)
# ─────────────────────────────────────────────────────────────────────────────

def main():
    # 1. Sum from 1 to 10
    print(f"Sum 1..10 = {sum(range(1, 11))}")

    # 2. Iterate over a list
    fruits = ["apple", "banana", "cherry"]
    for f in fruits:
        print(f"  {f}")

    # 3. enumerate
    for i, f in enumerate(fruits, 1):
        print(f"  {i}. {f}")

    # 4. Nested loops — 3×3 table
    for r in range(1, 4):
        for c in range(1, 4):
            print(f"  {r}x{c}={r*c}", end="  ")
        print()

if __name__ == "__main__":
    main()
