from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Optional, NumberRange, Email

class RegisterForm(FlaskForm):
    name = StringField("Full Name", validators=[DataRequired()])
    email = StringField("Email Address", validators=[DataRequired(), Email()])
    age = IntegerField("Age", validators=[DataRequired(), NumberRange(min=1, max=120)])
    submit = SubmitField("Register")

class UpdateForm(FlaskForm):
    name = StringField("Full Name", validators=[Optional()])
    email = StringField("Email Address", validators=[Optional(), Email()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=1, max=120)])
    submit = SubmitField("Update Profile")
