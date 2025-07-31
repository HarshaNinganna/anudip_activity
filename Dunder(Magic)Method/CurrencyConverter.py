class Currency:
    rates = {
        'USD': 1.0,
        'INR': 83.0,
        'EUR': 0.91
    }

    def __init__(self, amount, currency_type):
        self.amount = amount
        self.currency_type = currency_type.upper()

    def convert_to(self, target_currency):
        target_currency = target_currency.upper()
        base_amount = self.amount / Currency.rates[self.currency_type]
        converted = base_amount * Currency.rates[target_currency]
        return Currency(round(converted, 2), target_currency)

    def __add__(self, other):
        if self.currency_type != other.currency_type:
            raise ValueError("Cannot add different currencies without conversion")
        return Currency(self.amount + other.amount, self.currency_type)

    def __str__(self):
        return f"{self.amount} {self.currency_type}"

c1 = Currency(100, 'USD')
c2 = Currency(200, 'USD')
print(c1 + c2)                      
converted = c1.convert_to('INR')
print(converted)                      
