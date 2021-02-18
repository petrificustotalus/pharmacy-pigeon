from flask_wtf import FlaskForm
from wtforms import Form, StringField, SubmitField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Email

class SearchForm(Form):
    city = StringField('Miasto')
    drugname = StringField('Nazwa leku')


class ClientDataForm(FlaskForm):
    name = StringField('Imię', validators=[DataRequired()])
    surname = StringField('Nazwisko', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    phone = IntegerField('Telefon kontaktowy')
    address = StringField('Adres')
    quantity = IntegerField('Wprowadź liczbę opakowań', validators=[DataRequired()])
    prescription = BooleanField('Oświadczam że posiadam ważną receptę do zamówionych leków na receptę.')
    submit = SubmitField('Potwierdź dane')

