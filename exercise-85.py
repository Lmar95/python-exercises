# Exercise 85 — Program that tests the Syracuse (Collatz) conjecture
# Starting from any positive integer n:
#   if n is even  → n = n / 2
#   if n is odd   → n = 3n + 1
# The conjecture states the sequence always reaches 1.
# ─────────────────────────────────────────────────────────────────────────────

def syracuse(n: int) -> list:
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq

def main():
    n = int(input("Enter a positive integer: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        seq = syracuse(n)
        print(f"Sequence: {seq}")
        print(f"Length  : {len(seq)}")
        print(f"Maximum : {max(seq)}")

if __name__ == "__main__":
    main()
