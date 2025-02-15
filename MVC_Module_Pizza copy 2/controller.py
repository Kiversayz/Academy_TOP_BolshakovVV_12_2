class PizzeriaController:
    def __init__(self, model):
        self.model = model
    
    def add_order(self, pizza, toppings, price):
        return self.model.add_order(pizza, toppings, price)
    
    def get_orders(self):
        return self.model.get_orders()
    
    def get_stats(self):
        return self.model.get_stats()