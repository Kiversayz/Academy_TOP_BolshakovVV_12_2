class MovieController:
    def __init__(self, model):
        self.model = model
    
    def get_movie_info(self):
        """Получить информацию о фильме."""
        return self.model.get_movie_info()
    
    def update_movie_info(self, title, genre, director, year, duration, studio, actors):
        """Обновить информацию о фильме."""
        self.model.title = title
        self.model.genre = genre
        self.model.director = director
        self.model.year = year
        self.model.duration = duration
        self.model.studio = studio
        self.model.actors = actors
