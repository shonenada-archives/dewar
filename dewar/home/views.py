# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, url_for, redirect


home_app = Blueprint('home', __name__, template_folder="templates")


@home_app.route('/')
def index():
    return render_template('index.html')
