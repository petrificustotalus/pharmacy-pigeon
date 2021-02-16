from flask_wtf import FlaskForm
from wtforms import Form, StringField, SubmitField
from wtforms.validators import DataRequired, Email

class SearchForm(Form):
    city = StringField('Miasto')
    drugname = StringField('Nazwa leku')


class ClientDataForm(FlaskForm):
    name = StringField('Imię', validators=[DataRequired()])
    surname = StringField('Nazwisko', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    phone = StringField('Telefon kontaktowy')
    address = StringField('Adres')
    submit = SubmitField('Potwierdź dane')