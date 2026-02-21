# Exercise 35 — Program that calculates and displays the Fibonacci sequence
# F(0)=0, F(1)=1, F(n)=F(n-1)+F(n-2)
# ─────────────────────────────────────────────────────────────────────────────

def fibonacci(n: int) -> list:
    seq = [0, 1]
    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

def main():
    n = int(input("How many terms? "))
    if n <= 0:
        print("Enter a positive integer.")
    else:
        print(", ".join(map(str, fibonacci(n))))

if __name__ == "__main__":
    main()
