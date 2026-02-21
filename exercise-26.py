# Exercise 26 — Program with the while loop
# Computes the sum of integers from 1 to N using a while loop.
# ─────────────────────────────────────────────────────────────────────────────

def main():
    n = int(input("Enter N: "))
    total, i = 0, 1
    while i <= n:
        total += i
        i += 1
    print(f"Sum from 1 to {n} = {total}")

if __name__ == "__main__":
    main()
