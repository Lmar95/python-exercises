# Exercise 91 — Generate random data with the Faker module
# Requires: faker (pip install faker)
# ─────────────────────────────────────────────────────────────────────────────

def main():
    try:
        from faker import Faker
        fake = Faker()
        n = int(input("How many fake profiles to generate? "))
        print()
        for _ in range(n):
            print(f"Name    : {fake.name()}")
            print(f"Email   : {fake.email()}")
            print(f"Address : {fake.address()}")
            print(f"Job     : {fake.job()}")
            print("-" * 40)
    except ImportError:
        print("Faker not installed. Run: pip install faker")

if __name__ == "__main__":
    main()
