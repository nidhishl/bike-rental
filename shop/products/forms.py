from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import Form, IntegerField, StringField, BooleanField, TextAreaField, validators

class Addmodel(Form):
    company = StringField('Company', [validators.DataRequired()])
    model = StringField('Model', [validators.DataRequired()])
    modelno = IntegerField('Model Number', [validators.DataRequired()])
    image = FileField('Image', validators=[FileRequired(), FileAllowed(['jpg', 'jpeg', 'png'])])
    price = IntegerField('Price/Day', [validators.DataRequired()])