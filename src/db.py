import sqlite3

from interfaces import ReviewRepositoryInterface

DATABASE = "reviews.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    return conn


def init_db():
    with get_db() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                sentiment TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """
        )
        conn.commit()


class ReviewRepository(ReviewRepositoryInterface):
    def __init__(self):
        self.db = get_db()

    def create_data(
        self,
        text: str,
        sentiment: str,
        created_at: str,
    ) -> int:
        with self.db as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO reviews (
                    text, sentiment, created_at
                ) VALUES (
                    ?, ?, ?
                )
                """,
                (text, sentiment, created_at),
            )
            conn.commit()
        return cursor.lastrowid

    def get_data(
        self,
        sentiment: str = None,
    ) -> list[tuple[int, str, str, str]]:
        query = "SELECT id, text, sentiment, created_at FROM reviews"
        params = ()

        if sentiment:
            query += " WHERE sentiment = ?"
            params = (sentiment,)

        with self.db as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            reviews = cursor.fetchall()
        return reviews
