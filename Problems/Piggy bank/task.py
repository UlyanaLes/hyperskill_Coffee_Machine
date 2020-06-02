class PiggyBank:
    def __init__(self, dollars, cents):
        self.cents = cents % 100
        self.dollars = dollars + cents // 100

    def add_money(self, add_dollars, add_cents):
        self.dollars += (self.cents + add_cents) // 100 + add_dollars
        self.cents = (self.cents + add_cents) % 100
