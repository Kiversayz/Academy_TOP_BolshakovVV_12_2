class MovieView:
    def __init__(self, controller):
        self.controller = controller
    
    def display_movie_info(self):
        """Отображение информации о фильме."""
        movie_info = self.controller.get_movie_info()
        print(movie_info)
    
    def update_movie_info(self):
        """Обновление информации о фильме."""
        title = input("Введите название фильма: ")
        genre = input("Введите жанр фильма: ")
        director = input("Введите имя режиссера: ")
        year = int(input("Введите год выпуска: "))
        duration = int(input("Введите длительность фильма в минутах: "))
        studio = input("Введите студию: ")
        
        actors = []
        while True:
            actor_name = input("Введите имя актера (или оставьте пустым для завершения): ")
            if actor_name == "":
                break
            actor_role = input(f"Введите роль актера {actor_name}: ")
            actors.append((actor_name, actor_role))
        
        # Обновляем информацию о фильме через контроллер
        self.controller.update_movie_info(title, genre, director, year, duration, studio, actors)
        print("Информация о фильме обновлена!")



