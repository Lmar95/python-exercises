# Exercise 99 — Create a list containing the 6 vowels of the French alphabet
# ─────────────────────────────────────────────────────────────────────────────

def main():
    vowels = ["a", "e", "i", "o", "u", "y"]   # 6 vowels in French
    print(f"Vowels: {vowels}")
    print(f"Number of vowels: {len(vowels)}")

    # Check if a character is a vowel
    char = input("\nEnter a character: ").lower()
    if char in vowels:
        print(f"'{char}' IS a vowel.")
    else:
        print(f"'{char}' is NOT a vowel.")

if __name__ == "__main__":
    main()
