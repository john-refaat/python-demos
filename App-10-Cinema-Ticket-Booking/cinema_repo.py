import sqlite3

from examples import delete_seat
from domain import Seat


class CinemaRepo:

    def __init__(self):
        self.db = 'cinema.db'
        self.table = 'seat'

    def find_by_id(self, seat_id):
        connection = sqlite3.connect(self.db)
        with connection:
            cursor = connection.cursor()
            cursor.execute(f'SELECT * FROM {self.table} WHERE seat_id=?', [seat_id])
            found_record = cursor.fetchone()
            return Seat(*found_record)

    def book_seat(self, seat_id):
        connection = sqlite3.connect(self.db)
        with connection:
            cursor = connection.cursor()
            cursor.execute(f'UPDATE {self.table} SET taken=1 WHERE seat_id=?', [seat_id])
            connection.commit()

    def create_seat(self, seat_id, taken, price):
        connection = sqlite3.connect(self.db)
        with connection:
            cursor = connection.cursor()
            cursor.execute(f'INSERT INTO {self.table} VALUES (?, ?, ?)', [seat_id, taken, price])
            connection.commit()

    def delete_seat(self, seat_id):
        connection = sqlite3.connect(self.db)
        with connection:
            cursor = connection.cursor()
            cursor.execute(f'DELETE FROM {self.table} WHERE seat_id=?', [seat_id])
            connection.commit()

if __name__ == '__main__':
    repo = CinemaRepo()
    repo.create_seat('C3', 0, 80.0)
    print(repo.find_by_id('C3'))
    repo.book_seat('C3')
    print(repo.find_by_id('C3'))
    delete_seat('C3')
