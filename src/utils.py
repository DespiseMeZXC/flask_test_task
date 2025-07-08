from interfaces import AnalyzeSentimentInterface


class AnalyzeSentiment(AnalyzeSentimentInterface):
    def __init__(self):
        self.__positive_words = [
            "хорош",
            "люблю",
            "отличн",
            "прекрасн",
            "супер",
            "класс",
        ]
        self.__negative_words = [
            "плохо",
            "ненавижу",
            "ужасный",
            "кошмар",
            "разочарован",
        ]

    @property
    def positive_words(self):
        return self.__positive_words

    @property
    def negative_words(self):
        return self.__negative_words

    def analyze(self, text: str) -> str:
        text_lower = text.lower()
        for word in self.positive_words:
            if word in text_lower:
                return "positive"
        for word in self.negative_words:
            if word in text_lower:
                return "negative"
        return "neutral"
