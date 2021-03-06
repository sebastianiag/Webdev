from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, validators

class RegistrationForm(Form):
    username = TextField('username', [validators.Length(min=1, max=25),validators.Required()])
    email = TextField('email', [validators.Email(message="Invalid email"), validators.Length(min=6, max=25), validators.Required()])
    password = PasswordField('password', [validators.Length(min=6, max=25),validators.Required(), validators.EqualTo('confirm', message= 'Passwords must match')])
    confirm = PasswordField('Repeat Password')
    
class LoginForm(Form):
    username = TextField('username', [validators.Required()])
    password = PasswordField('password', [validators.Required()])
    remember_me = BooleanField('remember_me', default = True)

class UploadForm(Form):
    uri = TextField('uri', [validators.Required()])
