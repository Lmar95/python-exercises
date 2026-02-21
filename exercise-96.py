# Exercise 96 — Translate text from one language to another
# Requires: googletrans (pip install googletrans==4.0.0rc1)
# ─────────────────────────────────────────────────────────────────────────────

def translate_text(text: str, src: str = "auto", dest: str = "en") -> str:
    try:
        from googletrans import Translator
        translator = Translator()
        result     = translator.translate(text, src=src, dest=dest)
        return result.text
    except ImportError:
        return "googletrans not installed. Run: pip install googletrans==4.0.0rc1"

def main():
    text      = input("Enter text to translate      : ")
    src_lang  = input("Source language (e.g. fr, auto): ") or "auto"
    dest_lang = input("Target language (e.g. en, ar )  : ") or "en"
    translated = translate_text(text, src_lang, dest_lang)
    print(f"\nTranslation: {translated}")

if __name__ == "__main__":
    main()
