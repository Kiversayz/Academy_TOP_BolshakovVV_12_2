import json

class Pizzeria:
    def __init__(self, file_name="orders"):
        """Инициализация класса с хранилищем данных."""
        self.__orders = []
        self.file_name = fr'MVC_Module_Pizza\data\{file_name}_data.json'
        self.load_data()
    
    def load_data(self):
        """Загрузка данных из файла."""
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                self.__orders = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.__orders = []
    
    def save_data(self):
        """Сохранение данных в файл."""
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(self.__orders, file, ensure_ascii=False, indent=4)
    
    def add_order(self, pizza, toppings, price):
        """Добавление заказа."""
        order = {"pizza": pizza, "toppings": toppings, "price": price}
        self.__orders.append(order)
        self.save_data()
        return True
    
    def get_orders(self):
        """Получение списка заказов."""
        return self.__orders
    
    def get_stats(self):
        """Получение статистики (количество продаж, выручка)."""
        total_pizzas = len(self.__orders)
        total_revenue = sum(order['price'] for order in self.__orders)
        return total_pizzas, total_revenue

