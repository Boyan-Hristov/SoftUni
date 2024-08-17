from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class TestShoppingCart(TestCase):

    def setUp(self) -> None:
        self.cart = ShoppingCart("Kaufland", 200)

    def test_correct_init(self):
        self.assertEqual("Kaufland", self.cart.shop_name)
        self.assertEqual(200.0, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_shop_name_setter_no_capital_letter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "billa"
        self.assertEqual("Shop must contain only letters and must start with capital letter!",
                         str(ve.exception))

    def test_shop_name_setter_invalid_symbols_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "Magazin345"
        self.assertEqual("Shop must contain only letters and must start with capital letter!",
                         str(ve.exception))

    def test_add_to_cart_too_expensive_product_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("TV", 300)
        self.assertEqual("Product TV cost too much!", str(ve.exception))

    def test_add_to_cart_price_equal_to_max_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("Whiskey", 100)
        self.assertEqual("Product Whiskey cost too much!", str(ve.exception))

    def test_add_to_cart_success_product_added(self):
        result = self.cart.add_to_cart("Milk", 2.50)
        self.assertEqual("Milk product was successfully added to the cart!",
                         result)
        self.assertEqual(1, len(self.cart.products))
        self.assertEqual({"Milk": 2.5}, self.cart.products)

    def test_remove_from_cart_non_existent_product_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart("Milk")
        self.assertEqual("No product with name Milk in the cart!",
                         str(ve.exception))

    def test_remove_from_cart_success_product_removed(self):
        self.cart.add_to_cart("Milk", 2.50)
        self.assertEqual(1, len(self.cart.products))
        result = self.cart.remove_from_cart("Milk")
        self.assertEqual("Product Milk was successfully removed from the cart!",
                         result)
        self.assertEqual(0, len(self.cart.products))
        self.assertEqual({}, self.cart.products)

    def test_add_returns_new_object_with_added_name_and_budget(self):
        self.cart.add_to_cart("Milk", 2.50)
        self.cart.add_to_cart("Bread", 1.80)
        other = ShoppingCart("Online", 150)
        other.add_to_cart("Apples", 4.20)
        other.add_to_cart("Beer", 2.30)
        new_cart = self.cart.__add__(other)
        result = new_cart

        self.assertEqual("KauflandOnline", new_cart.shop_name)
        self.assertEqual(350, new_cart.budget)
        self.assertEqual(4, len(new_cart.products))
        self.assertEqual({"Milk": 2.5, "Bread": 1.8, "Apples": 4.2, "Beer": 2.3},
                         new_cart.products)
        self.assertEqual(new_cart, result)

    def test_buy_products_not_enough_budget_raises_value_error(self):
        self.cart.budget = 10
        self.cart.add_to_cart("Milk", 2.50)
        self.cart.add_to_cart("Meat", 13.00)
        self.cart.add_to_cart("Ice Cream", 6.50)
        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()
        self.assertEqual("Not enough money to buy the products! "
                         "Over budget with 12.00lv!", str(ve.exception))

    def test_buy_products_success(self):
        self.cart.add_to_cart("Milk", 2.50)
        self.cart.add_to_cart("Meat", 13.00)
        self.cart.add_to_cart("Ice Cream", 6.50)
        result = self.cart.buy_products()
        self.assertEqual('Products were successfully bought! Total cost: 22.00lv.',
                         result)


if __name__ == "__main__":
    main()
