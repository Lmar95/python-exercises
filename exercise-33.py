# Exercise 33 — The while loop (various demonstrations)
# ─────────────────────────────────────────────────────────────────────────────

def main():
    # Countdown
    c = 5
    while c >= 1:
        print(c); c -= 1
    print("Go!")

    # Digit sum
    n = int(input("Integer for digit sum: "))
    s, tmp = 0, abs(n)
    while tmp:
        s += tmp % 10; tmp //= 10
    print(f"Sum of digits of {n} = {s}")

if __name__ == "__main__":
    main()
