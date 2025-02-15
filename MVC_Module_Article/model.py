import json

class Article:
    def __init__(self):
        """ Создание класса с контейнером для хранения статей. """
        self.__articles = []

    def get_articles(self):
        """ Получить список статей. """
        return self.__articles

    def add_article(self, title, author, char_count, publication, description, file_name):
        """ Добавить статью с указанными параметрами и сохранить в файл. """
        if not self.check_article(title):
            data = {
                'title': title,
                'author': author,
                'char_count': char_count,
                'publication': publication,
                'description': description
            }
            self.__articles.append(data)
            self.update_json(file_name)
            return True
        return False

    def check_article(self, title):
        """ Проверить, существует ли статья с указанным названием. """
        return any(article['title'] == title for article in self.__articles)

    def find_article_by_title(self, search_title):
        """ Найти статью по названию. """
        for article in self.__articles:
            if article['title'].lower() == search_title.lower():
                return article
        return None
    
    def update_json(self, file_name):
        """ Сохранить данные в JSON-файл. """
        full_file_name = fr'MVC_Module_Article/data/{file_name}_articles.json'
        with open(full_file_name, 'w', encoding='utf-8') as fp:
            json.dump(self.__articles, fp, ensure_ascii=False, indent=4)
