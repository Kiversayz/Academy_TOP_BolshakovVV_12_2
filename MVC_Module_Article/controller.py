class ArticleController:
    FORBIDDEN = "Ошибка: недостаточно прав доступа."
    ERROR_VALUE = "Ошибка: неверный тип данных - "
    
    # Определение ролей и их разрешений
    USER_ROLES = {
        'admin': ['admin'],
        'editor': ['admin', 'editor'],
        'viewer': ['admin', 'editor', 'viewer']
    }

    def __init__(self, model):
        """ Инициализация контроллера с моделью статей. """
        self.model = model

    def get_articles_auth(self, role='viewer'):
        """ Получить список статей с проверкой прав доступа. """
        if role in self.USER_ROLES['viewer']:
            return self.model.get_articles()
        return self.FORBIDDEN

    def add_article_auth(self, title, author, char_count, publication, description, file_name, role='viewer'):
        """ Добавить статью с проверкой прав доступа и типов данных. """
        if role not in self.USER_ROLES['editor']:
            return self.FORBIDDEN
        if not all(isinstance(arg, str) for arg in [title, author, publication, description]):
            return self.ERROR_VALUE
        if not isinstance(char_count, int):
            return self.ERROR_VALUE + str(char_count)

        return self.model.add_article(title, author, char_count, publication, description, file_name)

    def find_article_auth(self, search_title, role='viewer'):
        """ Найти статью по названию с проверкой прав доступа. """
        if role not in self.USER_ROLES['viewer']:
            return self.FORBIDDEN
        return self.model.find_article_by_title(search_title)
