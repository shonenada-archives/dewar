# -*- coding: utf-8 -*-
from datetime import datetime

from flask.ext.login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from dewar.exts import db


class Account(db.Model, UserMixin):

    __tablename__ = 'account'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(128), nullable=True, unique=True)
    nickname = db.Column(db.String(30))
    gender = db.Column(db.Integer, default=0)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    updated = db.Column(db.DateTime,
                        default=datetime.utcnow,
                        onupdate=datetime.utcnow, )
    active = db.Column(db.Boolean, default=True)
    deleted = db.Column(db.Boolean, default=False)

    def __init__(self, *args, **kwargs):
        super(Account, self).__init__(*args, **kwargs)
        if 'password' in kwargs:
            self.change_password(kwargs['password'])

    def is_active(self):
        return self.active

    def change_password(self, raw_password):
        return generate_password_hash(raw_passwd)

    def check_password(self, raw_password):
        return check_password_hash(self.password, raw_password)
