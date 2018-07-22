class TaxRate:

    TAX_EXEMPT = 0.0
    SALES_TAX = 0.10
    IMPORT_DUTY = 0.05

    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

        if self.rate < 0:
            raise ValueError('TaxRate has to be equal or greater than 0!')

    def calculate_tax(self, price):
        return price * self.rate
