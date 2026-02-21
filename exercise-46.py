# Exercise 46 — Program that converts a decimal number to binary
# ─────────────────────────────────────────────────────────────────────────────

def to_binary(n: int) -> str:
    if n == 0: return "0"
    bits, num = [], abs(n)
    while num:
        bits.append(str(num % 2)); num //= 2
    result = "".join(reversed(bits))
    return f"-{result}" if n < 0 else result

def main():
    n = int(input("Enter a decimal integer: "))
    print(f"Binary: {to_binary(n)}")

if __name__ == "__main__":
    main()
