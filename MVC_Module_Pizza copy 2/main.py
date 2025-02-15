from model import Pizzeria
from controller import PizzeriaController
from view import PizzeriaView

def main():
    model = Pizzeria()
    controller = PizzeriaController(model)
    view = PizzeriaView(controller)
    
    while True:
        view.display_menu()
        choice = input("Ваш выбор: ")
        
        if choice == "1":
            view.order_pizza()
            print()
        elif choice == "2":
            view.order_pizza_menu()
            print()
        elif choice == "3":
            view.display_orders()
            print()
        elif choice == "4":
            view.display_stats()
            print()
        elif choice == "5":
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()