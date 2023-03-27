import math


class MoneyMachine:

    CURRENCY = "£"

    COIN_VALUES = {
        "fifties": 0.5,
        "twenties": 0.10,
        "tens": 0.05,
        "fives": 0.01,
        "twos": 0.02,
        "ones": 0.01

    }

    change = 0

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.money_received

    def calculate_change(self, change):

        fifties = math.floor(change / 0.5)
        change -= fifties * 0.5

        twenties = math.floor(change / 0.2)
        change -= twenties * 0.2

        tens = math.floor(change / 0.1)
        change -= tens * 0.1

        fives = math.floor(change / 0.05)
        change -= fives * 0.05

        twos = math.floor(change / 0.02)
        change -= twos * 0.02

        ones = math.floor(change / 0.01)
        change -= ones * 0.01

        print(f"Your change contains {fifties} 50p coins, {twenties} 20p coins, {tens} 10p coins, {fives} 5p coins, {twos} 2p coins and {ones} 1p coins\n  ")

    def make_payment(self, cost):
        """Returns True when payment is accepted, or False if insufficient."""
        self.process_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.calculate_change(change)
            self.profit += cost
            self.money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.money_received = 0
            return False



