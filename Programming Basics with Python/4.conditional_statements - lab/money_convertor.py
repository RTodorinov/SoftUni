from forex_python.converter import CurrencyRates

c = CurrencyRates()
amount = int(input('Enter currency amount: '))
print()

print("Type of currency: USD, EUR, BGN")
from_currency = input('From currency: ')
to_currency = input('To currency: ')

result = c.convert(from_currency, to_currency, amount)
print()

print(f"From currency {from_currency} < - > To currency {to_currency}")
print(f"Your money in {to_currency} is:{result:.2f}")
