#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import render_template

from . import capstone_app_blueprint


@capstone_app_blueprint.route('/')
def index():
    return render_template('capstone_app/index.html')