class Catalogue:

    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name):
        self.products.append(product_name)

    def get_by_letter(self, first_letter):
        return [product for product in self.products if product.startswith(first_letter)]

    def __repr__(self):
        items = sorted(self.products)
        new_line = "\n"
        return f"Items in the {self.name} catalogue:{new_line}{f'{new_line}'.join(items)}"


