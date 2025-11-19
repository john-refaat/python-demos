from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField

from flatmates_bill.flat import Bill, Flatmate

app = Flask(__name__)

class HomePage(MethodView):
    def __init__(self):
        self.title = "Home"

    def get(self):
        return render_template('index.html', title=self.title)

class BillFormPage(MethodView):
    def __init__(self):
        self.title = 'Bill Form'

    def get(self):
        form = BillForm()
        return render_template('bill_form_page.html', title=self.title,
                               billform=form)

    def post(self):
        form = BillForm(request.form)
        amount = float(form.amount.data)
        period = form.period.data

        bill = Bill(amount, period)
        name1 = form.name1.data
        name2 = form.name2.data
        flatmate1 = Flatmate(name1, int(form.days_in_house1.data))
        flatmate2 = Flatmate(name2, int(form.days_in_house2.data))

        amount_1 = flatmate1.pays(bill, flatmate2)
        amount_2 = flatmate2.pays(bill, flatmate1)

        print(f"{flatmate1.name} pays: ", amount_1)
        print(f"{flatmate2.name} pays: ", amount_2)

        return render_template('bill_form_page.html', title=self.title,
                               billform=form, name1=name1, name2=name2,
                               amount1=amount_1, amount2=amount_2,
                               result=True)

class ResultsPage(MethodView):
    def __init__(self):
        self.title = "Results"

    def get(self):
        return 'Results'



class BillForm(Form):

    amount = StringField('Bill Amount: ', default='100.00')
    period = StringField('Bill Period: ', default='December 2020')

    name1 = StringField('Name: ', default='Jahn')
    days_in_house1 = StringField('Days in House: ', default='20')

    name2 = StringField('Name: ', default='Mary')
    days_in_house2 = StringField('Days in House: ', default='12')

    button = SubmitField('Submit')


app.add_url_rule('/', view_func=HomePage.as_view('home'))
app.add_url_rule('/bill_form', view_func=BillFormPage.as_view('bill_form_page'))
## app.add_url_rule('/results', view_func=ResultsPage.as_view('results'))

app.run(debug=True)