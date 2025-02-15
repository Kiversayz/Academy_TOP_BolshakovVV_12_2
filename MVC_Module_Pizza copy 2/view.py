class PizzeriaView:
    def __init__(self, controller):
        self.controller = controller
        self.menu = [
            {'pizza': 'Пеперони',
            'toppings': 'Соус Терьяки',
            'price': 900.00},
            {'pizza': 'Маргарита',
            'toppings': 'Соус Барбекью',
            'price': 800.00},
            {'pizza': 'Четыре сыра',
            'toppings': '',
            'price': 500.00},
            ]
    
    def display_menu(self):
        print("Добро пожаловать в пиццерию!")
        print("1. Заказать свою пиццу")
        print("2. Заказать пиццу из меню")
        print("3. Посмотреть заказы")
        print("4. Посмотреть статистику (админ)")
        print("5. Выход")
    
    def order_pizza(self):
        pizza = input("Выберите пиццу (Маргарита, Пепперони, Четыре сыра и т.д.): ")
        toppings = input("Дополнительные топпинги (через запятую): ").split(",")
        price = float(input("Введите цену: "))
        
        if self.controller.add_order(pizza, toppings, price):
            print("Заказ успешно добавлен!")
        else:
            print("Ошибка оформления заказа.")
    
    def order_pizza_menu(self):
        print('_________________Меню_________________')
        for id in range(len(self.menu)):
            print(f'{id}. {self.menu[id]['pizza']} - {self.menu[id]['toppings']} {self.menu[id]['price']}')
        id = int(input("Выберите номер пиццы из меню : "))
        if self.controller.add_order(self.menu[id]['pizza'], self.menu[id]['toppings'].split(","), self.menu[id]['price']):
            print("Заказ успешно добавлен!")
        else:
            print("Ошибка оформления заказа.")
    
    def display_orders(self):
        orders = self.controller.get_orders()
        if orders:
            for order in orders:
                print(f"Пицца: {order['pizza']}, Топпинги: {', '.join(order['toppings'])}, Цена: {order['price']}")
        else:
            print("Заказов пока нет.")
    
    def display_stats(self):
        total_pizzas, total_revenue = self.controller.get_stats()
        print(f"Продано пицц: {total_pizzas}, Выручка: {total_revenue} руб.")


