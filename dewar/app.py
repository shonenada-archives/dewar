# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask._compat import string_types

from dewar.config import CONFIG
from dewar.exts import setup_database, setup_login


def create_app(import_name=None, config=None):
    app = Flask(import_name or __name__)

    app.config.from_object('dewar.settings')
    app.config.update(CONFIG)
    print CONFIG

    if isinstance(config, dict):
        app.config.update(config)

    print app.config

    setup_database(app)
    setup_login(app)

    return app
