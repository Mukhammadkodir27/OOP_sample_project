from abc import ABC, abstractmethod


class Currency(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def to_base_currency(self):
        pass

    @classmethod
    def from_base_currency(cls, amount):
        return cls(amount / cls.base_rate)

    def __str__(self):
        return f"{self.value:.2f} {self.__class__.__name__}"

    def __add__(self, other):
        if isinstance(other, Currency):
            base_value = self.to_base_currency() + other.to_base_currency()
            return USD.from_base_currency(base_value)
        raise ValueError("Can only add Currency types")


class USD(Currency):
    base_rate = 1.0  # USD to USD conversion rate

    def to_base_currency(self):
        return self.value  # Already in USD


class EUR(Currency):
    base_rate = 1.18  # EUR to USD conversion rate

    def to_base_currency(self):
        return self.value * EUR.base_rate


class GBP(Currency):
    base_rate = 1.31  # GBP to USD conversion rate

    def to_base_currency(self):  # Corrected method name
        return self.value * GBP.base_rate


def main():
    print("Currency Conversion App")
    print("1. USD")
    print("2. EUR")
    print("3. GBP")
    choice = int(input("Choose your currency (1-3): "))

    amount = float(input("Enter amount in chosen currency: "))

    if choice == 1:
        currency = USD(amount)
    elif choice == 2:
        currency = EUR(amount)
    elif choice == 3:
        currency = GBP(amount)
    else:
        print("Invalid choice!")
        return

    print(
        f"Amount in base currency (USD): {currency.to_base_currency():.2f} USD")

    # Demo: Convert to another currency
    if isinstance(currency, USD):
        new_currency = EUR.from_base_currency(currency.to_base_currency())
        print(f"Converted to EUR: {new_currency}")
    elif isinstance(currency, EUR):
        new_currency = GBP.from_base_currency(
            currency.to_base_currency())  # Corrected method name
        print(f"Converted to GBP: {new_currency}")
    elif isinstance(currency, GBP):
        new_currency = USD.from_base_currency(currency.to_base_currency())
        print(f"Converted to USD: {new_currency}")


if __name__ == "__main__":
    main()
