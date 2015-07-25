# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, url_for, redirect


account_app = Blueprint('account', __name__, wrl_prefix='/account',
                        template_folder='templates')


@account_app.route('/signin', methods=['GET', 'POST'])
def signin():
    return render_template('account/signin.html')


@account_app.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('account/signup.html')


@account_app.route('/signout', methods=['POST'])
def signout():
    return redirect(url_for('home.index'))
