from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField
from wtforms.fields.html5 import DateTimeField, DateField
from datetime import datetime

class Addbooking(Form):
    startTime = DateField('', [validators.DataRequired()])
    endTime = DateField('', [validators.DataRequired()])
    # d = DateField('Date', [validators.DataRequired()], default=datetime.today)
    # pickup = StringField('Pick up Location', [validators.DataRequired()])
    # phno = StringField('Phone Number', [validators.DataRequired()])
    # modelno = IntegerField('Model Number', [validators.DataRequired()])