from app.domainmodel.movie import Movie
from app.domainmodel.review import Review


class User:
    def __init__(self, user_name: str, password: str):
        if (user_name == "" or type(user_name) is not str) and \
                (password == "" or type(password) is not str):
            self.__user_name = None
            self.__password = None
        else:
            self.__user_name = user_name.strip().lower()
            self.__password = password.strip()
            self.__watched_movies = []
            self.__reviews = []
            self.__time_spent = 0

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        return self.__user_name == other.__user_name

    def __lt__(self, other):
        return self.__user_name < other.__user_name

    def __hash__(self):
        return hash(self.__user_name)

    @property
    def user_name(self):
        return self.__user_name

    @user_name.setter
    def user_name(self, new_name: str):
        self.__user_name = new_name

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def watched_movies(self):
        return self.__watched_movies

    @watched_movies.setter
    def watched_movies(self, movie: Movie):
        self.__watched_movies.append(movie)

    @property
    def reviews(self):
        return self.__reviews

    @reviews.setter
    def reviews(self, review: Review):
        self.__reviews.append(review)

    @property
    def time_spent_watching_movies_minutes(self):
        return self.__time_spent

    @time_spent_watching_movies_minutes.setter
    def time_spent_watching_movies_minutes(self, minutes: int):
        self.__time_spent += minutes

    def watch_movie(self, movie: Movie):
        self.__watched_movies.append(movie)
        self.__time_spent += movie.runtime_minutes

    def add_review(self, review: Review):
        self.__reviews.append(review)


class TestUserMethods:

    def test_init(self):
        user1 = User('han', '1q2w3e4r')
        user2 = User('aron', 'a4t5g5')
        users = [user1, user2]
        assert users[0] == user1
