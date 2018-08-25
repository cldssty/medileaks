# -*- coding: utf-8 -*-
"""Medileaks app and app method definitions.
    
   Todo:
       1. Replace MongoDB and sql with elasticsearch.
       2. Add remaining app methods.
       
"""

import os

from flask import Flask, render_template
from flask_pymongo import PyMongo


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase" 
    mongo = PyMongo(app)

    app.config.from_mapping(
        SECRET_KEY='dev', 
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    @app.route('/home')
    def home():
        return render_template('home.html')

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import search # why is it complaining?
    app.register_blueprint(search.bp)

    return app
