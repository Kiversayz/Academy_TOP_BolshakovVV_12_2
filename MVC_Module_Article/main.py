import controller
import model
import view

def main():
    """ Главная функция, реализующая взаимодействие пользователя с системой статей. """
    
    # Инициализация MVC-компонентов
    article_model = model.Article()
    article_controller = controller.ArticleController(article_model)
    article_view = view.ArticleView(article_controller)
    
    # Приветственное сообщение
    article_view.display_welcome_message()
    
    # Выбор роли пользователя
    role = input("Какая ваша роль? (admin, editor, viewer): ").strip().lower()
    
    while True:
        print("\nВыберите действие:")
        print("1. Просмотреть список статей")
        print("2. Добавить статью")
        print("3. Найти статью по названию")
        print("4. Выход")

        choice = input("Ваш выбор: ").strip()

        if choice == '1':  
            # Просмотр всех статей
            article_view.display_articles_auth(role)

        elif choice == '2':  
            # Добавление новой статьи
            title = input("Название статьи: ").strip()
            author = input("Автор статьи: ").strip()
            char_count = input("Количество знаков: ").strip()
            
            # Проверка, является ли число целым
            if not char_count.isdigit():
                print("Ошибка: количество знаков должно быть числом.")
                continue
            
            char_count = int(char_count)
            publication = input("Издание/Сайт публикации: ").strip()
            description = input("Краткое описание: ").strip()
            file_name = input("Имя файла для хранения: ").strip()

            article_view.post_add_article_auth(title, author, char_count, publication, description, file_name, role)

        elif choice == '3':  
            # Поиск статьи по названию
            search_title = input("Введите название статьи для поиска: ").strip()
            article_view.find_article(search_title, role)

        elif choice == '4':  
            # Выход из программы
            print("Выход из программы.")
            break

        else:
            print("Ошибка: Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()


