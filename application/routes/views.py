"""
A module for views in the application-routes package.
"""

from flask import Blueprint, render_template

bp: Blueprint = Blueprint("views", __name__)


@bp.route("/")
def index() -> str:
    """
    Path operation for the index template
    :return: The rendered template
    :rtype: str
    """
    return render_template("index.html")
