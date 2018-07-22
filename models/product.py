from models.product_category import ProductCategory
from models.product_origin import ProductOrigin


class Product:

    def __init__(self, name, category, origin, price):
        self.name = name
        self.category = category
        self.origin = origin
        self.price = price

        if self.price <= 0:
            raise ValueError('Price has to be greater than 0!')

        if not type(self.origin) == ProductOrigin:
            raise TypeError('Invalid origin!')

        if not type(self.category) == ProductCategory:
            raise TypeError('Invalid category!')

    def calculate_tax(self):
        return self.category.calculate_tax(self.price) + self.origin.calculate_tax(self.price)
