from flask_wtf import FlaskForm as Form
from wtforms import TextField, PasswordField, IntegerField, HiddenField
from wtforms.validators import DataRequired, Length, Email, URL


class RegisterForm(Form):
    name = TextField(
            'Tell us your name:',
            validators=[DataRequired(message="Name is required"),
                        Length(min=3, message="Name must greater than 3 chars")]
    )
    email = TextField(
            'Enter your E-mail:',
            validators=[DataRequired("E-mail is required"), Email(message="Invalid E-mail address")]
    )
    password = PasswordField(
            'Password:',
            validators=[DataRequired("Password is required")]
    )
    country_code = TextField(
            'Country Code:',
            validators=[Length(min=1, max=4, message="Country code must be between 1 and 4 numbers")]
    )

    phone_number = IntegerField(
            'Phone Number:',
            validators=[DataRequired("Valid phone number is required")]
    )


class LoginForm(Form):
    email = TextField(
            'E-mail:',
            validators=[DataRequired("E-mail is required"), Email(message="Invalid E-mail address")]
    )
    password = PasswordField(
            'Password:',
            validators=[DataRequired("Password is required")]
    )


class VacationPropertyForm(Form):
    description = TextField(
            'Description:',
            validators=[DataRequired("Description is required")]
    )
    image_url = TextField(
            'Image URL:',
            validators=[DataRequired("Image Url required"), URL(message="Invalid Image Url")]
    )


class ReservationForm(Form):
    message = TextField(
            'Message:',
            validators=[DataRequired("Message is required")]
    )

    property_id = HiddenField()


class ReservationConfirmationForm(Form):
    From = TextField('From:')
    Body = TextField('Body')
