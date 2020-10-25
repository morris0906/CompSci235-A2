import app.domainmodel.movie as movies


class Actor:
    def __init__(self, actor_full_name: str):
        if actor_full_name == "" or type(actor_full_name) is not str:
            self.__actor_full_name = None
        else:
            self.__actor_full_name = actor_full_name.strip()
            self.__colleague = []
            self.__actor_movies = []

    @property
    def actor_full_name(self) -> str:
        return self.__actor_full_name

    @property
    def actor_movies(self):
        return self.__actor_movies

    def add_movie(self, movie: movies):
        self.__actor_movies.append(movie)

    def is_related(self, movie: movies) -> bool:
        return movie in self.__actor_movies

    def __repr__(self):
        return f"<Actor {self.__actor_full_name}>"

    def __eq__(self, other):
        if not isinstance(other, Actor):
            return False
        return self.__actor_full_name == other.__actor_full_name

    def __lt__(self, other):
        return self.__actor_full_name < other.__actor_full_name

    def __hash__(self):
        return hash(self.__actor_full_name)

    def add_actor_colleague(self, colleague):
        if isinstance(colleague, Actor):
            self.__colleague.append(colleague)

    def check_if_this_actor_worked_with(self, colleague):
        return colleague in self.__colleague


class TestActor:

    def test_init(self):
        actor1 = Actor("Han Lee")
        actor2 = Actor("Alan Waker")
        actor1.add_actor_colleague(actor2)
        assert actor1.check_if_this_actor_worked_with_colleague(actor2) == True
        actor3 = Actor("Taika Waititi")
        assert repr(actor3) == "<Actor Taika Waititi>"
        actor4 = Actor("")
        assert actor4.actor_full_name is None
        actor5 = Actor(42)
        assert actor5.actor_full_name is None
