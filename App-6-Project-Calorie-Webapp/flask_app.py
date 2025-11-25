from flask import Flask, render_template, request
from flask.views import MethodView
from wtforms import Form, StringField, SubmitField
from wtforms.fields.numeric import IntegerField
from wtforms.validators import DataRequired, NumberRange

from calories import Calories
from temperature import Temperature

app = Flask(__name__)


class HomePage(MethodView):
    def get(self):
        return render_template('index.html')


class CaloriesForm(Form):
    weight = IntegerField("Weight: ", default=75, validators=[DataRequired(), NumberRange(min=0, max=500)])
    height = IntegerField("Height: ", default=178, validators=[DataRequired(), NumberRange(min=0, max=300)])
    temperature = IntegerField(
        "Temperature in degrees Celsius: ", default=20, validators=[DataRequired(), NumberRange(min=-20, max=50)]
    )

    age = IntegerField("Age: ", default=37, validators=[DataRequired(), NumberRange(min=0, max=120)])
    country = StringField("Country: ", default="egypt", validators=[DataRequired()])
    city = StringField("City: ", default="sharm-el-sheikh", validators=[DataRequired()])
    button = SubmitField("Calculate")


class CaloriesPage(MethodView):
    def get(self):
        calories_form = CaloriesForm()
        return render_template('calories_form_page.html', caloriesform=calories_form)

    def post(self):
        calories_form = CaloriesForm(request.form)
        if calories_form.validate():
            weight = calories_form.weight.data
            height = calories_form.height.data
            age = calories_form.age.data
            country = calories_form.country.data
            city = calories_form.city.data
            temperature = Temperature(country, city).get()
            calories = Calories(weight, height, age, temperature).calculate()
            return render_template('calories_form_page.html', caloriesform=calories_form, calories=calories,
                                   result=True)
        return render_template('calories_form_page.html', caloriesform=calories_form, error="Invalid input",
                               result=False)


app.add_url_rule('/', view_func=HomePage.as_view('home'))
app.add_url_rule('/calories_form', view_func=CaloriesPage.as_view('calories_form_page'))

if __name__ == '__main__':
    app.run(debug=True)
