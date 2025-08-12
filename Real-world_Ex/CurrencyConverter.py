import requests

def convert_currency(base, target, amount):
    try:
        url = f"https://api.exchangerate.host/convert?from={base.upper()}&to={target.upper()}&amount={amount}"
        response = requests.get(url)
        data = response.json()

        if data.get("result") is None:
            print(" Invalid currency code or API error.")
            return None

        return data["result"], data["info"]["rate"]

    except requests.exceptions.RequestException as e:
        print(" Error fetching data:", e)
        return None


if __name__ == "__main__":
    print(" Currency Converter — Live Exchange Rates")

    base_currency = input("Enter base currency (e.g., USD): ").strip()
    target_currency = input("Enter target currency (e.g., INR): ").strip()

    try:
        amount = float(input("Enter amount to convert: "))
    except ValueError:
        print(" Invalid amount.")
        exit()

    result = convert_currency(base_currency, target_currency, amount)

    if result:
        converted_amount, rate = result
        print(f"\n Exchange Rate: 1 {base_currency.upper()} = {rate:.2f} {target_currency.upper()}")
        print(f" {amount} {base_currency.upper()} = {converted_amount:.2f} {target_currency.upper()}")
