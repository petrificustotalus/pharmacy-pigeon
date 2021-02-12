from wtforms import Form, StringField


class SearchForm(Form):
    city = StringField('Miasto')
    drugname = StringField('Nazwa leku')