from flask import Blueprint, request, jsonify
from constant import AUTHTOKEN

api_blueprint = Blueprint("api_blueprint", __name__)

@api_blueprint.before_request
def auth():
    authenticated = False
    if "x-auth-token" not in request.headers:
        return jsonify({"error": "Invalid request"}), 401
    for auth in AUTHTOKEN:
        if AUTHTOKEN[auth] == request.headers["x-auth-token"]:
            authenticated = True
            break
    if not authenticated:
        return jsonify({"error": "Unauthorized"}), 401


@api_blueprint.route("/data")
def index():
    return [
        "data1", "data2"
    ]
