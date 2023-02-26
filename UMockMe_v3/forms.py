from flask_wtf import FlaskForm
from wtforms import IntegerField,SubmitField,RadioField,SelectField,StringField,PasswordField
from wtforms import validators, ValidationError

class NewAccount(FlaskForm):
    email = StringField("Email Address",[validators.DataRequired("Please enter your email address."),
      validators.Email("Please enter your email address.")])
    userName = StringField("User screen Name",[validators.DataRequired("Please enter Screen Name.")])
    Password = PasswordField("Password",[validators.DataRequired("Please enter your password.")])



    FavoriteTeam = SelectField('Favorite Team',id='FavoriteTeam')
    Fname = StringField("First Name",[validators.DataRequired("Please enter your first name.")])
    Lname = StringField("Last Name",[validators.DataRequired("Please enter your last name.")])

    submit = SubmitField("Submit")



class Login(FlaskForm):
    email = StringField("Email Address", [validators.DataRequired("Please enter your email address."),
                                          validators.Email("Please enter a valid email address.")])
    Password = PasswordField("Password", [validators.DataRequired("Please enter your password.")])
    submit = SubmitField("Login")