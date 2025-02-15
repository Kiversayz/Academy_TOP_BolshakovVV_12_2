from model import Movie
from controller import MovieController
from view import MovieView

def main():
    # Инициализация фильма с первоначальными данными
    movie = Movie(
        title="Пример фильма",
        genre="Драма",
        director="Иван Иванов",
        year=2025,
        duration=120,
        studio="КиноМечта",
        actors=[("Алексей Смирнов", "Главная роль"), ("Мария Петрова", "Второстепенная роль")]
    )
    
    # Создание контроллера и представления
    controller = MovieController(movie)
    view = MovieView(controller)
    
    # Основной цикл программы
    while True:
        print("\n1. Посмотреть информацию о фильме")
        print("2. Обновить информацию о фильме")
        print("3. Выход")
        
        choice = input("Ваш выбор: ")
        
        if choice == "1":
            view.display_movie_info()  # Показать информацию о фильме
        elif choice == "2":
            view.update_movie_info()  # Обновить информацию о фильме
        elif choice == "3":
            break  # Завершить программу
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
