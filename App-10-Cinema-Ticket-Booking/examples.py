import sqlite3


def select_all(db_path: str = "cinema.db") -> None:
    connection = sqlite3.connect(db_path)
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM "seat"')
        print(cursor.fetchall())
    finally:
        connection.close()


def find_by_id(seat_id: str, db_path: str = "cinema.db"):
    connection = sqlite3.connect(db_path)
    try:
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM "seat" WHERE "seat_id"=?', (seat_id,))
        return cursor.fetchone()
    finally:
        connection.close()


def save_seat(seat_id: str, taken: int, price: float, db_path: str = "cinema.db"):
    connection = sqlite3.connect(db_path)
    try:
        with connection:
            cursor = connection.cursor()
            cursor.execute('INSERT INTO "seat" VALUES (?, ?, ?)', (seat_id, taken, price))
    finally:
        connection.close()


def update_seat(seat_id: str, taken: int, price: float, db_path: str = "cinema.db"):
    connection = sqlite3.connect(db_path)
    try:
        with connection:
            cursor = connection.cursor()
            cursor.execute('UPDATE "seat" SET "taken"=?, "price"=? WHERE "seat_id"=?', (taken, price, seat_id))
    finally:
        connection.close()

def delete_seat(seat_id: str, db_path: str = "cinema.db"):
    connection = sqlite3.connect(db_path)
    try:
        with connection:
            cursor = connection.cursor()
            cursor.execute('DELETE FROM "seat" WHERE "seat_id"=?', (seat_id,))
            print("Deleted seat with id: " + seat_id)
            return cursor.rowcount
    finally:
        connection.close()


if __name__ == "__main__":
    delete_seat("C1")
    select_all()
    print(find_by_id("A2"))
    save_seat("C1", 0, 80.0)
    select_all()
    update_seat("C1", 1, 80.0)
    print(find_by_id("C1"))