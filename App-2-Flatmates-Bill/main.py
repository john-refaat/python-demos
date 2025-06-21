import webbrowser

from flat import Bill, Flatmate
from reports import PdfReport

if __name__ == '__main__':
    amount = float(input("Hey user, enter the bill amount: "))
    period = input("What is the bill period? E.g. December 2020: ")
    n = int(input("How many flatmates are there? "))
    bill = Bill(amount, period)
    for i in range(n):
        name = input(f"What is the name of flatmate {i+1}? ")
        days_in_house = int(input(f"How many days did {name} stay in the house during the bill period? "))
        bill.add_flatmate(Flatmate(name, days_in_house))

    for flat_mate in bill.flatmates:
        print(f"{flat_mate.name} pays: {flat_mate.pays(bill)}")
    file_path = f'files/bill-{bill.period}.pdf'
    report = PdfReport(filename=file_path)
    report.generate(bill)
    webbrowser.open(file_path)
