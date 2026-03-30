import unittest
from unittest.mock import MagicMock
from carte_pizzeria import CartePizzeria
from carte_pizzeria_exception import CartePizzeriaException

class TestCartePizzeria(unittest.TestCase):

    def setUp(self):
        self.carte = CartePizzeria()
        self.pizza_mock = MagicMock()
        self.pizza_mock.name = "Margherita"

    # Tests is_empty()
    def test_is_empty_carte_vide(self):
        self.assertTrue(self.carte.is_empty())

    def test_is_empty_carte_non_vide(self):
        self.carte.add_pizza(self.pizza_mock)
        self.assertFalse(self.carte.is_empty())

    # Tests nb_pizzas()
    def test_nb_pizzas_carte_vide(self):
        self.assertEqual(self.carte.nb_pizzas(), 0)

    def test_nb_pizzas_une_pizza(self):
        self.carte.add_pizza(self.pizza_mock)
        self.assertEqual(self.carte.nb_pizzas(), 1)

    # Tests add_pizza()
    def test_add_pizza(self):
        self.carte.add_pizza(self.pizza_mock)
        self.assertEqual(self.carte.nb_pizzas(), 1)

    # Tests remove_pizza()
    def test_remove_pizza_existante(self):
        self.carte.add_pizza(self.pizza_mock)
        self.carte.remove_pizza("Margherita")
        self.assertEqual(self.carte.nb_pizzas(), 0)

    def test_remove_pizza_inexistante(self):
        with self.assertRaises(CartePizzeriaException):
            self.carte.remove_pizza("Inconnue")

if __name__ == "__main__":
    unittest.main()