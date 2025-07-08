from abc import ABC, abstractmethod
from flask import jsonify


class AnalyzeSentimentInterface(ABC):
    @abstractmethod
    def analyze(self, text: str) -> str:
        pass


class ReviewRepositoryInterface(ABC):
    @abstractmethod
    def create_data(
        self,
        text: str,
        sentiment: str,
        created_at: str,
    ) -> int:
        pass

    @abstractmethod
    def get_data(
        self,
        sentiment: str = None,
    ) -> list[tuple[int, str, str, str]]:
        pass


class ReviewServiceInterface(ABC):
    @abstractmethod
    def create_data(self, text: str) -> jsonify:
        pass

    @abstractmethod
    def get_data(self, sentiment: str = None) -> jsonify:
        pass
