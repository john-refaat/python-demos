class Bill:
    """
    Object that contains data about a bill, such as total amount and period of the bill.
    """
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period
        self.flatmates = []

    def add_flatmate(self, flatmate):
        self.flatmates.append(flatmate)

    def total_days(self):
        return sum([flatmate.days_in_house for flatmate in self.flatmates])


class Flatmate:
    """
    Creates a flatmate person who lives in the flat and pays a share of the bill.
    """
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        weight = self.days_in_house / bill.total_days()
        return bill.amount * weight
