# -*- coding: utf-8 -*-
from flask import Blueprint


account_app = Blueprint(__name__, 'account', url_prefix='/account')


@account_app.route('')
def index():
    pass


@account_app.route('/signin', methods=['GET', 'POST'])
def signin():
    pass


@account_app.route('/signup', methods=['GET', 'POST'])
def signup():
    pass


@account_app.route('/signout', methods=['POST'])
def signout():
    pass
