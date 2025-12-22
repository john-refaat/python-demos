from cinema_repo import CinemaRepo
from domain import Ticket
from fin_repo import FinRepo




def book_ticket(name, seat_id):
    cinema_repo = CinemaRepo()
    fin_repo = FinRepo()
    seat = cinema_repo.find_by_id(seat_id)

    if not seat or seat.taken == 1:
        print('Seat is not available')
        return None

    print('Price is ' + str(seat.price) + '')
    answer = input('Confirm purchase? (y/n)')
    if answer != 'y':
        print('Purchase cancelled')
        return None
    card_number = input('Please enter your card number: ')
    if not fin_repo.check_card_num(card_number):
        print('Card number is invalid')
        return None
    holder_name = input('Please enter card holder name: ')
    cvc = input('Please enter CVC: ')
    if fin_repo.withdraw(card_number, cvc, holder_name, seat.price) == 0:
        print('Transaction failed. Please try again.')
        return None
    cinema_repo.book_seat(seat_id)
    print('Purchase successful')
    return Ticket(seat_id, seat.id, name, seat.price)



if __name__ == '__main__':
    while True:
        name = input('Please enter your name: ')
        print('Hello ' + name + '!')
        seat_id = input('Select seat: ')
        ticket = book_ticket(name, seat_id)
        if ticket:
            print(ticket)
        else:
            print('Purchase failed.')
        print()

