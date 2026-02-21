"""\
# Exercise 9 — Program that converts duration into hours, minutes, and seconds
# ─────────────────────────────────────────────────────────────────────────────

def convert(total_seconds: int) -> tuple:
    hours   = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return hours, minutes, seconds

def main():
    s = int(input("Enter a duration in seconds: "))
    if s < 0:
        print("Duration must be positive.")
    else:
        h, m, sec = convert(s)
        print(f"\\n{s}s = {h}h {m}m {sec}s")

if __name__ == "__main__":
    main()
"""
