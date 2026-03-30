from pizza import Pizza
from carte_pizzeria_exception import CartePizzeriaException

class CartePizzeria:
    def __init__(self):
        self.pizzas = []

    def is_empty(self) -> bool:
        return len(self.pizzas) == 0

    def nb_pizzas(self) -> int:
        return len(self.pizzas)

    def add_pizza(self, pizza: Pizza):
        self.pizzas.append(pizza)

    def remove_pizza(self, name: str):
        for pizza in self.pizzas:
            if pizza.name == name:
                self.pizzas.remove(pizza)
                return
        raise CartePizzeriaException(name)

    def __repr__(self):
        return f"CartePizzeria(pizzas={self.pizzas})"