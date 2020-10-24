import csv
import re

from app.domainmodel.movie import Movie
from app.domainmodel.actor import Actor
from app.domainmodel.genre import Genre
from app.domainmodel.director import Director


class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__movies = []
        self.__actors = []
        self.__genres = []
        self.__directors = []

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            for row in movie_file_reader:
                title = row['Title']
                release_year = int(row['Year'])
                movie = Movie(title, release_year)
                movie.votes = row['Votes']
                movie.metascore = row['Metascore']
                movie.rating = row['Rating']
                movie.description = row['Description']
                self.__movies.append(movie)
                director = Director(row['Director'])
                if director not in self.__directors:
                    self.__directors.append(director)
                actors = re.split(", |,", row["Actors"])
                for actor_splited in actors:
                    actor = Actor(actor_splited)
                    if actor not in self.__actors:
                        self.__actors.append(actor)
                genres = row['Genre'].split(",")
                for genre_splited in genres:
                    genre = Genre(genre_splited)
                    if genre not in self.__genres:
                        self.__genres.append(genre)

    @property
    def dataset_of_movies(self):
        return self.__movies

    @property
    def dataset_of_actors(self):
        return self.__actors

    @property
    def dataset_of_directors(self):
        return self.__directors

    @property
    def dataset_of_genres(self):
        return self.__genres


dataset = MovieFileCSVReader("C:/Users/Owner/Downloads/235/CS235FlixSkeleton/datafiles/Data1000Movies.csv")
dataset.read_csv_file()
print(f'number of unique movies: {len(dataset.dataset_of_movies)}')
print(f'number of unique actors: {len(dataset.dataset_of_actors)}')
print(f'number of unique directors: {len(dataset.dataset_of_directors)}')
print(f'number of unique genres: {len(dataset.dataset_of_genres)}')
a = dataset.dataset_of_movies[0]
print(a, a.metascore, a.rating, a.votes, a.description)
