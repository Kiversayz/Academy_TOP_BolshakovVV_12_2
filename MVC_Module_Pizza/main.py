import json
from abc import ABC, abstractmethod

# Абстрактный класс для создания пиццы
class Pizza(ABC):
    def __init__(self, name, base_price):
        self.name = name
        self.base_price = base_price
        self.toppings = []
        self.price = base_price
    
    def add_topping(self, topping):
        """ Добавлениие топпинга """
        self.toppings.append(topping)
        self.price += 50  # Цена увеличивается за каждый добавленный топпинг
    
    def __str__(self):
        """ Вывод информации о пицце """
        toppings_str = ', '.join(self.toppings) if self.toppings else 'Без топпингов'
        return f"{self.name} ({toppings_str}) - {self.price} руб."

# Фабричный метод для создания стандартных и кастомных пицц
class PizzaFactory:
    MENU = {
        1: ("Маргарита", 800),
        2: ("Пепперони", 900),
        3: ("Четыре сыра", 1000),
        4: ("Гавайская", 850),
        5: ("Мясная", 950)
    }

    @staticmethod
    def create_pizza(choice, custom_name=None, custom_price=None):
        if choice in PizzaFactory.MENU:
            name, price = PizzaFactory.MENU[choice]
            return Pizza(name, price)
        elif choice == 6 and custom_name and custom_price:
            return Pizza(custom_name, max(custom_price, 500))  # Минимальная цена 500 руб.
        else:
            raise ValueError("Некорректный выбор пиццы.")

# Класс для управления заказами
class Pizzeria:
    def __init__(self, file_name="orders"):
        self.orders = []
        self.file_name = f"MVC_Module_Pizza\data\{file_name}.json"
        self.load_data()
    
    def load_data(self):
        """ Загружаем историю заказов """
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                self.orders = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.orders = []
    
    def save_data(self):
        """ Сохраняем в историю заказ """
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(self.orders, file, ensure_ascii=False, indent=4)
    
    def add_order(self, pizza):
        """ Добавление заказа """
        order = {"pizza": pizza.name, "toppings": pizza.toppings, "price": pizza.price}
        self.orders.append(order)
        self.save_data()
    
    def get_stats(self):
        """ Получить данные о статистике """
        classic_count = 0
        custom_count = 0
        revenue = 0
        toppings_count = {}
        
        for order in self.orders:
            revenue += order["price"]
            if order["pizza"] in [name for name, _ in PizzaFactory.MENU.values()]:
                classic_count += 1
            else:
                custom_count += 1
            for topping in order["toppings"]:
                toppings_count[topping] = toppings_count.get(topping, 0) + 1
        
        return classic_count, custom_count, revenue, toppings_count

# Основная программа
if __name__ == "__main__":
    pizzeria = Pizzeria()
    
    while True:
        print("\nМеню пицц:")
        for num, (name, price) in PizzaFactory.MENU.items():
            print(f"{num}. {name} - {price} руб.")
        print("6. Создать свою пиццу")
        print("7. Посмотреть заказы")
        print("8. Статистика продаж")
        print("9. Выход")
        
        try:
            choice = int(input("Выберите действие: "))
        except ValueError:
            print("Некорректный ввод. Попробуйте снова.")
            continue
        
        if choice in range(1, 6):
            pizza = PizzaFactory.create_pizza(choice)
        elif choice == 6:
            name = input("Введите название вашей пиццы: ")
            while True:
                try:
                    price = int(input("Введите цену вашей пиццы (не менее 500 руб.): "))
                    if price < 500:
                        print("Цена не может быть ниже 500 руб. Попробуйте снова.")
                        continue
                    break
                except ValueError:
                    print("Некорректный ввод. Введите число.")
            pizza = PizzaFactory.create_pizza(6, custom_name=name, custom_price=price)
        elif choice == 7:
            for order in pizzeria.orders:
                print(f"{order['pizza']} ({', '.join(order['toppings']) if order['toppings'] else 'Без топпингов'}) - {order['price']} руб.")
            continue
        elif choice == 8:
            classic, custom, revenue, toppings_count = pizzeria.get_stats()
            print(f"Продано классических пицц: {classic}")
            print(f"Продано кастомных пицц: {custom}")
            print(f"Выручка: {revenue} руб.")
            print("Популярные топпинги:")
            for topping, count in toppings_count.items():
                print(f"{topping}: {count} раз")
            continue
        elif choice == 9:
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")
            continue
        
        add_topping = input("Хотите добавить топпинги? (да/нет): ").lower()
        if add_topping == "да":
            while True:
                topping = lower(input("Введите название топпинга (или 'стоп' для завершения): "))
                if topping.lower() == "стоп":
                    break
                pizza.add_topping(topping)
        
        pizzeria.add_order(pizza)
        print(f"Заказ добавлен: {pizza}")
