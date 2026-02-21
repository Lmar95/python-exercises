# Exercise 24 — Program that returns the type of a character
# ─────────────────────────────────────────────────────────────────────────────

def char_type(c: str) -> str:
    if c.isalpha():  return "Alphabetic"
    if c.isdigit():  return "Digit"
    if c.isspace():  return "Whitespace"
    return "Special character"

def main():
    c = input("Enter a single character: ")
    if len(c) != 1:
        print("Please enter exactly one character.")
    else:
        print(f"'{c}' → {char_type(c)}")

if __name__ == "__main__":
    main()
