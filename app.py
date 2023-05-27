from flask import Flask, render_template, request, jsonify
from data_bp import api_blueprint
from constant import AUTHTOKEN

app = Flask(__name__)

MOCK_SUCCESS_TOKENS = [
    "abc",
    "xyz"
]


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.route("/auth", methods=["POST"])
def auth():
    data = request.get_json()
    if data["token"] in MOCK_SUCCESS_TOKENS:
        return jsonify({"auth": AUTHTOKEN[data['token']]}), 200
    return jsonify({"auth": "failed"}), 401

app.register_blueprint(
    api_blueprint,
    url_prefix="/api",
)


if __name__ == "__main__":
    app.run(debug=True)
