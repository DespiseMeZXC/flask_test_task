from datetime import datetime, timezone
from flask import jsonify

from db import ReviewRepository
from utils import AnalyzeSentiment
from interfaces import ReviewServiceInterface


class ReviewService(ReviewServiceInterface):
    def __init__(self):
        self.review_repository = ReviewRepository()
        self.analyze_sentiment = AnalyzeSentiment()

    def create_data(self, text: str) -> jsonify:
        sentiment = self.analyze_sentiment.analyze(text)
        created_at = datetime.now(timezone.utc).isoformat()
        review_id = self.review_repository.create_data(
            text,
            sentiment,
            created_at,
        )
        return (
            jsonify(
                {
                    "id": review_id,
                    "text": text,
                    "sentiment": sentiment,
                    "created_at": created_at,
                }
            ),
            201,
        )

    def get_data(self, sentiment: str = None) -> jsonify:
        reviews = self.review_repository.get_data(sentiment)
        return jsonify(
            [
                {
                    "id": row[0],
                    "text": row[1],
                    "sentiment": row[2],
                    "created_at": row[3],
                }
                for row in reviews
            ]
        )
