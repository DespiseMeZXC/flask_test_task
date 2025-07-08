from flask import Flask, request, jsonify

from db import init_db
from services import ReviewService

app = Flask(__name__)


@app.route("/reviews", methods=["POST"])
def create_review():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Invalid data"}), 400

    return ReviewService().create_data(data["text"])


@app.route("/reviews", methods=["GET"])
def get_reviews():
    sentiment_filter = request.args.get("sentiment")
    return ReviewService().get_data(sentiment_filter)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
