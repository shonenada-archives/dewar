# -*- coding: utf-8 -*-
from flask.ext.login import LoginManager, current_user


from dewar.account.models import Account


login_manager = LoginManager()


def setup_login(app):
    login_manager.init_app(app)


@login_manager.user_loader
def load_account(account_id):
    return Account.query.get(account_id)
