#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask

app = Flask(__name__)


def create_app():
    from capstone_app import capstone_app_blueprint
    app.register_blueprint(capstone_app_blueprint)
    return app