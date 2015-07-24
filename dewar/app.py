# -*- coding: utf-8 -*-
import os

from flask import Flask
from flask._compat import string_types

from dewar.exts import setup_database, setup_login


def create_app(import_name=None, config=None):
    app = Flask(import_name or __name__)

    app.config.from_object('dewar.settings')

    if isinstance(config, dict):
        app.config.update(config)
    elif isinstance(config, string_types):
        app.config.from_pyfile(os.path.abspath(config))

    setup_database(app)
    setup_login(app)

    return app
