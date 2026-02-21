# Exercise 98 — Program that fills and displays a list of 10 items
# ─────────────────────────────────────────────────────────────────────────────

def main():
    n    = 10
    data = []
    print(f"Enter {n} values:")
    for i in range(1, n + 1):
        val = input(f"  Item {i}: ")
        data.append(val)
    print("\nYour list:")
    for idx, item in enumerate(data, 1):
        print(f"  [{idx}] {item}")

if __name__ == "__main__":
    main()
