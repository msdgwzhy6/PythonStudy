from wtforms import Form, StringField, validators

class CalcForm(Form):
    w = StringField("w", [validators.DataRequired()])
    h = StringField("h", [validators.DataRequired()])