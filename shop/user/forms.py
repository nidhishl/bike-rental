from wtforms import Form, BooleanField, StringField, PasswordField, validators

class RegistrationForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    licenseNo = StringField('License Number', [validators.Length(min=4, max=6)])
    phno = StringField('Phone Number', [validators.Length(min=10, max=13)])
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

class LoginForm(Form):
    phno = StringField('Phone Number', [validators.Length(min=10, max=13)])
    password = PasswordField('Password', [validators.DataRequired()])
