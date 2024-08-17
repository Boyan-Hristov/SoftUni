from typing import List
from project.client import Client
from project.meals.meal import Meal


class FoodOrdersApp:
    VALID_MEALS = ["Starter", "MainDish", "Dessert"]
    RECEIPT_ID = 0

    def __init__(self):
        self.menu: List[Meal] = []
        self.clients_list: List[Client] = []

    def register_client(self, client_phone_number: str):
        try:
            next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
            raise Exception("The client has already been registered!")

        except StopIteration:
            client = Client(client_phone_number)
            self.clients_list.append(client)
            return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        # debug to test
        valid_meals = [m for m in meals if m.__class__.__name__ in self.VALID_MEALS]
        if valid_meals:
            self.menu.extend(valid_meals)

    def show_menu(self):
        # debug to test
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        return "\n".join([m.details() for m in self.menu])

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        # debug to test
        try:
            client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        except StopIteration:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        meals_in_menu = [m.name for m in self.menu]
        meals_info = {}

        for meal, quantity in meal_names_and_quantities.items():
            if meal not in meals_in_menu:
                raise Exception(f"{meal} is not on the menu!")

            meal_object = next(filter(lambda m: m.name == meal, self.menu))
            meals_info[meal_object] = quantity

        for m, q in meals_info.items():
            if q > m.quantity:
                raise Exception(f"Not enough quantity of {m.__class__.__name__}: {m.name}!")

        for key, value in meals_info.items():
            client.shopping_cart.append(key)
            client.bill += key.price * value
            key.quantity -= value

        return f"Client {client_phone_number} successfully ordered " \
               f"{', '.join(m.name for m in client.shopping_cart)} " \
               f"for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for meal in client.shopping_cart:
            meal.quantity += meal.INITIAL_QUANTITY - meal.quantity
        client.shopping_cart.clear()
        client.bill = 0

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = next(filter(lambda c: c.phone_number == client_phone_number, self.clients_list))
        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        paid_money = client.bill
        client.shopping_cart.clear()
        client.bill = 0
        self.RECEIPT_ID += 1

        return f"Receipt #{self.RECEIPT_ID} with total amount of {paid_money:.2f} " \
               f"was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals " \
               f"on the menu and {len(self.clients_list)} clients."

