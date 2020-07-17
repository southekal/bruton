from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import (
	FileField,
	FileAllowed,
	FileRequired
)
from sqlalchemy import func
from wtforms import (
	IntegerField,
	PasswordField,
	SelectField,
	SelectMultipleField,
	StringField,
	SubmitField,
	TextAreaField
)
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.fields.html5 import EmailField
from wtforms.validators import (
	Email,
	DataRequired,
	ValidationError
)
from wtforms.widgets import html5

from helper import db as db_helper

from log_config.custom_logger import logger


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email Address', validators=[DataRequired(), Email()])
    org = StringField('Organization', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Get Started')

    def validate_org(self, org):
        pass

    def validate_email(self, email):
        user_record = db_helper.get_user(email=email.data)
        if user_record is not None:
            logger.warning(f"user already exists; {user_record}; input; {email.data}")
            raise ValidationError('Please use a different email address.')


class LoginForm(FlaskForm):
    email = EmailField('Email Address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

