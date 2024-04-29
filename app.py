"""
Flask main application.
"""

from flask import Flask

from application.config import settings
from application.routes import api, views


def create_app() -> Flask:
    """
    Create a Flask application
    :return: Flask instance
    :rtype: Flask
    """
    flask: Flask = Flask(__name__)
    flask.register_blueprint(views.bp)
    flask.register_blueprint(api.bp)
    return flask


if __name__ == "__main__":
    app: Flask = create_app()
    app.run(host=settings.SERVER_HOST.__str__(), debug=settings.DEBUG_MODE)
