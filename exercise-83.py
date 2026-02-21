# Exercise 83 — Functions cos() and sin() from the math module
# Plots a simple text-based sine wave in the terminal.
# ─────────────────────────────────────────────────────────────────────────────

import math

WIDTH = 60

def text_sine_wave(periods: int = 2):
    steps = periods * 60
    for i in range(steps):
        angle = 2 * math.pi * i / 60
        y     = math.sin(angle)
        col   = int((y + 1) / 2 * (WIDTH - 1))
        print(" " * col + "*")

def main():
    print("Sine wave (text art):")
    text_sine_wave()

if __name__ == "__main__":
    main()
