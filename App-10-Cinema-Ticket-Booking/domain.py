class Ticket:

    def __init__(self, id, seat_id, name, price):
        self.id = id
        self.seat_id = seat_id
        self.name = name
        self.price = price

    def __repr__(self):
        return f'{self.id}: {self.seat_id} - {self.name} - {self.price}'


class Seat:
    def __init__(self, id, taken, price):
        self.id = id
        self.taken = taken
        self.price = price

    def __repr__(self):
        return f'{self.id}: {self.taken} - {self.price}'