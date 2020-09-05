from wtforms import Form, StringField, PasswordField, validators

class LoginForm(Form):
    phno = StringField('Phone Number', [validators.Length(min=10, max=13)])
    password = PasswordField('Password', [validators.DataRequired()])
