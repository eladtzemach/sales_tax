from ext import round_tax
from models.product import Product


class OrderItem:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

        if self.quantity <= 0:
            raise ValueError('Quantity has to be greater than 0!')

        if not type(self.product) == Product:
            raise TypeError('Invalid product!')

        self.total_price = self.quantity * self.product.price
        self.total_tax = self.product.calculate_tax() * self.quantity
        self.total_amount = self.total_price + float(round_tax(self.total_tax))
