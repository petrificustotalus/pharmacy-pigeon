from flask_wtf import FlaskForm
from wtforms import Form, StringField, SubmitField, IntegerField, BooleanField, SelectField, TextField
from wtforms.validators import DataRequired, Email

class SearchForm(FlaskForm):
    city = SelectField('Miasto', choices=['Białystok'])
    drugname = TextField('Nazwa leku', validators=[DataRequired()], id='drugname_autocomplete')


class ClientDataForm(FlaskForm):
    name = StringField('Imię', validators=[DataRequired()])
    surname = StringField('Nazwisko', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    phone = IntegerField('Telefon kontaktowy')
    address = StringField('Adres')
    quantity = IntegerField('Wprowadź liczbę opakowań', validators=[DataRequired()])
    prescription = BooleanField('Oświadczam że posiadam ważną receptę do zamówionych leków na receptę.', validators=[DataRequired()])
    rodo = BooleanField('Zostałam/-em się z dokumentem Informacja Administratora w związku z przetwarzaniem' + 
    'danych na potrzeby dokonania rezerwacji za pośrednictwem aplikacji Medivisor – zgodnie' 
    'z art. 13 ust. 1 i 2 Rozporządzenia Parlamentu Europejskiego i Rady (UE) 2016/679 z dnia 27 kwietnia 2016 r. w sprawie ochrony osób fizycznych w związku z przetwarzaniem' 
    'danych osobowych i w sprawie swobodnego przepływu takich danych oraz uchylenia dyrektywy 95/46/WE (zwanego dalej RODO)',  validators=[DataRequired()])
    submit = SubmitField('Potwierdź dane')

