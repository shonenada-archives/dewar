# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import InputRequired, Email, Length, EqualTo


class SignUpForm(Form):
	username = StringField(
		label=_('username'),
		validators=[
		    InputRequired(),
		    Length(min=3, max=30),
		]
	)
	email = EmailField(
		label=_('email'),
		validators=[
			InputRequired(),
			Email(),
		]
	)
	password = PasswordField(
		label=_('password'),
		validators=[
		    InputRequired(),
		    Length(min=6, max=30),
		]
	)
	confirm = PasswordField(
		label=_('confirm password'),
		validators=[
			InputRequired(),
			EqualTo('password'),
		]
	)