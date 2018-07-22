from models.tax_rate import TaxRate


class ProductOrigin:

    LOCAL = 'local'
    IMPORTED = 'imported'

    def __init__(self, name, tax_rate):
        self.name = name
        self.tax_rate = tax_rate

        if not type(self.tax_rate) == TaxRate:
            raise TypeError('Invalid tax rate!')

    def calculate_tax(self, price):
        return self.tax_rate.calculate_tax(price)
