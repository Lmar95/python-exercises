# Exercise 90 — Send a WhatsApp message, search on Google, etc. (automation demo)
# Requires: pywhatkit (pip install pywhatkit)
# ─────────────────────────────────────────────────────────────────────────────
# NOTE: This exercise showcases library usage. Run it in a real environment
#       with an active browser session for full functionality.

def send_whatsapp(phone: str, message: str, hour: int, minute: int):
    try:
        import pywhatkit
        pywhatkit.sendwhatmsg(phone, message, hour, minute)
        print("WhatsApp message scheduled.")
    except ImportError:
        print("pywhatkit not installed. Run: pip install pywhatkit")

def google_search(query: str):
    try:
        import pywhatkit
        pywhatkit.search(query)
        print(f"Searching Google for: {query}")
    except ImportError:
        print("pywhatkit not installed. Run: pip install pywhatkit")

def main():
    choice = input("1) Google search  2) Schedule WhatsApp message\nChoice: ")
    if choice == "1":
        query = input("Search query: ")
        google_search(query)
    elif choice == "2":
        phone   = input("Phone number (+countrycode): ")
        message = input("Message: ")
        hour    = int(input("Hour (24h): "))
        minute  = int(input("Minute   : "))
        send_whatsapp(phone, message, hour, minute)

if __name__ == "__main__":
    main()
