from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, PasswordField
from wtforms import validators
from wtforms.fields.html5 import EmailField

class CrunchForm(Form):
    hashtag = StringField('Hash Tag', validators=[validators.DataRequired()])