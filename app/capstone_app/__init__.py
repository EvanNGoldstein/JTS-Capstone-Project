#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Blueprint

capstone_app_blueprint = Blueprint('capstone_app', __name__)

from . import views