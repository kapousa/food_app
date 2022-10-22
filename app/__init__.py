# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import logging
from configparser import ConfigParser

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module

db = SQLAlchemy(session_options={"expire_on_commit": False})


config_parser = ConfigParser()
config_parser.read('properties.properties')


def register_extensions(app):
    db.init_app(app)


def register_blueprints(app):
    for module_name in ('foodsearch', 'base'):
        module = import_module('app.{}.routes'.format(module_name))
        app.register_blueprint(module.blueprint)


def configure_database(app):
    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    logging.basicConfig(filename='bm_log.log', level=logging.ERROR)
    register_extensions(app)
    register_blueprints(app)
    configure_database(app)
    # print(config_parser.get('ErrorMessages', 'ErrorMessages.fail_create_model'))
    return app
