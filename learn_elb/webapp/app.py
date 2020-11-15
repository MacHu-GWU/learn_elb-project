# -*- coding: utf-8 -*-

from flask import Flask
from . import (
    _index,
)

def create_app():
    app = Flask("learn-elb")
    app.register_blueprint(_index.bp)
    return app
