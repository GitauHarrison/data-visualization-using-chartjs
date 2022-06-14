from logging import PlaceHolder
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField, \
    BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo, \
    ValidationError
from app.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1, 64),
                                             Email()])
    username = StringField('Username', validators=[
        DataRequired(), Length(1, 64),
        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
               'Usernames must have only letters, numbers, dots or '
               'underscores')])
    password = PasswordField('Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')


class MeanScore(FlaskForm):
    term = IntegerField(
        'Term',
        validators=[DataRequired()],
        render_kw={"placeholder": 'e.g. "1"'})
    math = IntegerField(
        'Math',
        validators=[DataRequired()],
        render_kw={"placeholder": 'e.g. "66"'})
    english = IntegerField(
        'English',
        validators=[DataRequired()],
        render_kw={"placeholder": 'e.g. "66"'})
    science = IntegerField(
        'Science',
        validators=[DataRequired()],
        render_kw={"placeholder": 'e.g. "66"'})
    ict = IntegerField(
        'ICT',
        validators=[DataRequired()],
        render_kw={"placeholder": 'e.g. "66"'})
    history = IntegerField(
        'History',
        validators=[DataRequired()],
        render_kw={"placeholder": 'e.g. "66"'})
    submit = SubmitField('Submit')
