""" The main app package constructor, containing the app factory function"""

from flask import Flask
from app.frontend import frontend as frontend_blueprint


def create_app(config_name):
    """ Factory function which creates an application object.

    Args:
        config_name: Name of the configuration object to use.
                Available options are: 'test', 'production',
                'development', and 'default'.
    Returns:
        app: configured application.
    """

    app = Flask(__name__)

    register_blueprints(app)

    return app


def register_blueprints(app):
    """ Registers the Flask blueprints

    Args:
        app: Flask application instance.
    """
    app.register_blueprint(frontend_blueprint)
