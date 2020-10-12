""" Init method for cle_parcel_lookup module """

from flask import Flask
from . import cle_parcel_lookup


def create_app():
    """ create_app is the main entrypoint """
    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(cle_parcel_lookup.bp)
    app.add_url_rule('/', endpoint='index')

    return app
