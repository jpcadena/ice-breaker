"""
A module for api in the application-routes package.
"""

from flask import Blueprint, jsonify, request
from flask.wrappers import Response

from application.services.ice_breaker import ice_break_with

bp: Blueprint = Blueprint("api", __name__)


@bp.route("/process", methods=["POST"])
def process() -> Response:
    """
    Process the LLM request for IceBreaker
    :return: The Flask response from the server
    :rtype: Response
    """
    name: str = request.form["name"]
    (
        summary_and_facts,
        interests,
        ice_breakers,
        profile_pic_url,
    ) = ice_break_with(name)
    return jsonify(
        {
            "summary_and_facts": summary_and_facts.model_dump(),
            "interests": interests.model_dump(),
            "ice_breakers": ice_breakers.model_dump(),
            "picture_url": profile_pic_url,
        }
    )
