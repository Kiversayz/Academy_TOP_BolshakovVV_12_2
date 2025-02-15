class ArticleView:
    FORBIDDEN = "Ошибка: недостаточно прав доступа."

    def __init__(self, controller):
        """ Инициализация представления с контроллером статей. """
        self.controller = controller

    def display_welcome_message(self):
        """ Отобразить приветственное сообщение. """
        print("Добро пожаловать в систему управления статьями!")

    def display_articles_auth(self, role='viewer'):
        """ Отобразить список статей с проверкой прав доступа. """
        articles = self.controller.get_articles_auth(role)
        
        if articles == self.FORBIDDEN:
            print(self.FORBIDDEN)
            return

        if articles:
            print("\nСписок доступных статей:")
            for article in articles:
                print(f"\nНазвание: {article['title']}\n"
                      f"Автор: {article['author']}\n"
                      f"Количество знаков: {article['char_count']}\n"
                      f"Издание: {article['publication']}\n"
                      f"Описание: {article['description']}\n")
        else:
            print("Нет доступных статей.")

    def post_add_article_auth(self, title, author, char_count, publication, description, file_name, role='viewer'):
        """ Добавить статью с проверкой прав доступа. """
        result = self.controller.add_article_auth(title, author, char_count, publication, description, file_name, role)

        if result is True:
            print(f"Статья '{title}' успешно добавлена.")
        elif result is False:
            print(f"Статья '{title}' уже существует.")
        elif result == self.FORBIDDEN:
            print(self.FORBIDDEN)
        else:
            print(result)  # Вывод ошибки в случае неправильного типа данных

    def find_article(self, search_title, role='viewer'):
        """ Найти статью по названию с проверкой прав доступа. """
        article = self.controller.find_article_auth(search_title, role)
        
        if article == self.FORBIDDEN:
            print(self.FORBIDDEN)
            return

        if article:
            print(f"\nНайденная статья:\n"
                  f"Название: {article['title']}\n"
                  f"Автор: {article['author']}\n"
                  f"Количество знаков: {article['char_count']}\n"
                  f"Издание: {article['publication']}\n"
                  f"Описание: {article['description']}\n")
        else:
            print(f"Статья с названием '{search_title}' не найдена.")

