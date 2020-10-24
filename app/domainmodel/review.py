from datetime import datetime

from app.domainmodel.movie import Movie


class Review:
    def __init__(self, input_movie: Movie, review_text: str, input_rating: int):
        if input_rating < 0 or input_rating > 10:
            self.__rating = None
        else:
            self.__reviewText = review_text
            self.__rating = input_rating
            now = datetime.now()
            self.__timestamp = datetime.timestamp(now)
            self.__movie = input_movie

    def __repr__(self):
        return self.__movie + f"Review: {self.__reviewText}, Rating: {self.__rating}"

    def __eq__(self, other):
        return (self.__rating == other.__rating) and (self.__movie == other.__movie) \
               and (self.__timestamp == other.__timestamp) and (self.__reviewText == other.__reviewText)

    @property
    def movie(self):
        return self.__movie

    @property
    def review_text(self):
        return  self.__reviewText

    @property
    def rating(self):
        return self.__rating

    @property
    def timestamp(self):
        return self.__timestamp
