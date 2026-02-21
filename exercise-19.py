# Exercise 19 — Program that calculates the price including tax (TTC)
# ─────────────────────────────────────────────────────────────────────────────

def price_ttc(ht: float, rate: float) -> float:
    return ht * (1 + rate / 100)

def main():
    ht   = float(input("Price excl. tax (HT)   : "))
    rate = float(input("VAT rate (%) e.g. 20   : "))
    ttc  = price_ttc(ht, rate)
    print(f"\nHT  : {ht:.2f}")
    print(f"VAT : {ht * rate / 100:.2f}")
    print(f"TTC : {ttc:.2f}")

if __name__ == "__main__":
    main()
