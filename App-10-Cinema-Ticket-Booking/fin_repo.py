import sqlite3


class FinRepo:

    def __init__(self):
        self.db = 'banking.db'
        self.table = 'Card'


    def check_card_num(self, card_number):
        connection = sqlite3.connect(self.db)
        with connection:
            cursor = connection.cursor()
            cursor.execute(f'SELECT count(*) FROM {self.table} WHERE number=?', [card_number])
            return cursor.fetchone()[0]

    def check_balance(self, card_number, cvc, holder, amount):
        connection = sqlite3.connect(self.db)
        with connection:
            cursor = connection.cursor()
            cursor.execute(f'SELECT count(*) FROM {self.table} WHERE number=? AND cvc=? AND holder=? AND balance>=?', [card_number, cvc, holder, amount])
            return cursor.fetchone()[0]

    def withdraw(self, card_number, cvc, holder, amount):
        connection = sqlite3.connect(self.db)
        with connection:
            cursor = connection.cursor()
            cursor.execute(f'UPDATE {self.table} SET balance=balance-{amount} WHERE number=? AND cvc=? AND holder=? AND balance>=?', [card_number, cvc, holder, amount])
            return cursor.rowcount

    def select_all(self):
        connection = sqlite3.connect(self.db)
        with connection:
            cursor = connection.cursor()
            cursor.execute(f'SELECT * FROM {self.table}')
            return cursor.fetchall()

if __name__ == '__main__':
    fin_repo = FinRepo()
    print(fin_repo.check_card_num('23456789'))
    print(fin_repo.check_balance('23456789', '235', 'Marry Smith', 100))
    print(fin_repo.select_all())
    print(fin_repo.withdraw('23456789', '235', 'Marry Smith', 100))
    print(fin_repo.select_all())
    print('-------------------------------')
    print(fin_repo.check_card_num('23456781'))
    print(fin_repo.check_balance('23456781', '235', 'Marry Smith', 100))
    print(fin_repo.select_all())
    print(fin_repo.withdraw('23456781', '235', 'Marry Smith', 100))
    print(fin_repo.select_all())
    print('-------------------------------')
    print(fin_repo.check_card_num('23456789'))
    print(fin_repo.check_balance('23456789', '235', 'Marry Smith', 9000))
    print(fin_repo.select_all())
    print(fin_repo.withdraw('23456789', '235', 'Marry Smith', 9000))
    print(fin_repo.select_all())

