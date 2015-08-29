# -*- coding: utf-8 -*-
from flask.ext.babel import lazy_gettext as _
from flask.ext.wtf import Form
from wtforms import StringField, EmailField, PasswordField
from wtforms.validators import InputRequired, Email, Length, EqualTo


class SignUpForm(Form):

    username = StringField(
        label=_(u'username'),
        validators=[
            InputRequired(),
            Length(min=3, max=60),
        ]
    )
    password = PasswordField(
        label=_(u'password'),
        validators=[
            InputRequired(),
            Length(min=6, max=30),
        ]
    )
    email = EmailField(
        label=_(u'email'),
        validators=[
            InputRequired(),
            Email(),
        ]
    )
    nickname = StringField(
        label=_(u'nickname'),
        validators=[
            InputRequired(),
            Length(min=3, max=30),
        ]
    )
    confirm = PasswordField(
        label=_(u'confirm password'),
        validators=[
            InputRequired(),
            EqualTo('password'),
        ]
    )

    def validate_username(form, field):
        query_user = Account.query.filter_by(username=field.data)
        if query_user.count() > 0:
            raise ValidatorError(_(u'username exists'))

    def validate_email(form, field):
        query_user = Account.query.filter_by(email=field.data)
        if query_user.count() > 0:
            raise ValidatorError(_(u'Email exists'))


class SignInForm(Form):

    username = StringField(
        label=_(u'username'),
        validators=[
            InputRequired(),
            Length(min=3, max=60),
        ]
    )
    passowrd = PasswordField(
        label=_(u'password'),
        validators=[
            InputRequired(),
            Length(min=6, max=30),
        ],
    )


class ResetPassword(Form):

    old_password = PasswordField(
        label=_(u'old password'),
        validators=[
            InputRequired(),
        ],
    )
    new_password = PasswordField(
        label=_(u'new password'),
        validators=[
            InputRequired(),
            Length(min=6, max=30),
        ]
    )
    confirm = PasswordField(
        label=_(u'confirm password'),
        validators=[
            EqualTo('new_password'),
        ]
    )
