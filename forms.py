from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


# RegistrationForm inherit from FlaskForm
# 'Username' w 'Email' w kda de labels ele htzhr ll user
# validators de restriction 3la el ktaba
# DataRequired w length w kol da 3obara 3n classes
# DataRequired() ---> menf3sh tb2a fadea
# Email() ---> make sure email is valid
# EqualTo('password') ---> lazm tkon ze el password
# SubmitField('Sign Up') ---> bersl el info ll asl

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')