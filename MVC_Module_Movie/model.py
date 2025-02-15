class Movie:
    def __init__(self, title, genre, director, year, duration, studio, actors):
        """Инициализация класса с информацией о фильме."""
        self.title = title
        self.genre = genre
        self.director = director
        self.year = year
        self.duration = duration
        self.studio = studio
        self.actors = actors  # Список актеров, каждый элемент - это кортеж (ФИО, роль)

    def get_movie_info(self):
        """Возвращает полную информацию о фильме."""
        actors_info = ', '.join([f"{actor[0]} как {actor[1]}" for actor in self.actors])
        return f"Название: {self.title}\nЖанр: {self.genre}\nРежиссер: {self.director}\n" \
               f"Год выпуска: {self.year}\nДлительность: {self.duration} минут\n" \
               f"Студия: {self.studio}\nАктеры: {actors_info}"

