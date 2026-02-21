# Exercise 92 — Convert text to speech with pyttsx3
# Requires: pyttsx3 (pip install pyttsx3)
# ─────────────────────────────────────────────────────────────────────────────

def text_to_speech(text: str, rate: int = 150, volume: float = 1.0):
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.setProperty("rate",   rate)
        engine.setProperty("volume", volume)
        engine.say(text)
        engine.runAndWait()
    except ImportError:
        print("pyttsx3 not installed. Run: pip install pyttsx3")

def main():
    text = input("Enter text to convert to speech: ")
    text_to_speech(text)

if __name__ == "__main__":
    main()
