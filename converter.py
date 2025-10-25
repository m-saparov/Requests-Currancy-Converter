import sys
import requests

usd_data = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/USD/").json()[0]
euro_data = requests.get("https://cbu.uz/uz/arkhiv-kursov-valyut/json/EUR/").json()[0]

usd_rate = float(usd_data["Rate"])
euro_rate = float(euro_data["Rate"])

while True:
    print(
        "\n-----MENU-----\n"
        "1. USD to UZS\n"
        "2. EURO to UZS\n"
        "3. UZS to EURO\n"
        "4. UZS to USD\n"
        "5. Exit\n"
    )

    choice = input("Enter choice: ")

    if choice == "1":
        try:
            usd = float(input("Enter USD: "))
            uzs = usd * usd_rate
            print(f"${usd} = {uzs:,.2f} so'm")
        except ValueError:
            print("USD faqat son bo'lishi kerak!")

    elif choice == "2":
        try:
            euro = float(input("Enter EURO: "))
            uzs = euro * euro_rate
            print(f"€{euro} = {uzs:,.2f} so'm")
        except ValueError:
            print("EURO faqat son bo'lishi kerak!")

    elif choice == "3":
        try:
            uzs = float(input("Enter UZS: "))
            euro = uzs / euro_rate
            print(f"{uzs:,.2f} so'm = €{euro:.2f}")
        except ValueError:
            print("UZS faqat son bo'lishi kerak!")

    elif choice == "4":
        try:
            uzs = float(input("Enter UZS: "))
            usd = uzs / usd_rate
            print(f"{uzs:,.2f} so'm = ${usd:.2f}")
        except ValueError:
            print("UZS faqat son bo'lishi kerak!")

    elif choice == "5":
        print("Good-Bye.")
        sys.exit()
    else:
        print("Bunday tanlov mavjud emas!")
