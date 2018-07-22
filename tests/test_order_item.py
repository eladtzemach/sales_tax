import unittest

from models.order_item import OrderItem
from models.product import Product
from models.product_category import ProductCategory
from models.product_origin import ProductOrigin

from models.tax_rate import TaxRate


class TestOrderItem(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create tax types
        # TaxRate(name, rate)
        tax_exempt = TaxRate("TAX_EXEMPT", TaxRate.TAX_EXEMPT)
        sales_tax = TaxRate("SALEX_TAX", TaxRate.SALES_TAX)

        # create item categories
        # ProductCategory(name, TaxRate)
        cls.books = ProductCategory(ProductCategory.BOOKS, tax_exempt)
        other = ProductCategory(ProductCategory.OTHER, sales_tax)

        # create the additional local/imported tax types
        # ProductOrigin(name, TaxRate)
        local = ProductOrigin(ProductOrigin.LOCAL, tax_exempt)

        cls.product = Product("music CD", other, local, 10)
        cls.order_one = OrderItem(cls.product, 1)
        cls.order_two = OrderItem(cls.product, 2)

    @classmethod
    def tearDownClass(cls):
        pass

    # invalid quantity, invalid product
    def test_constructor(self):
        self.assertRaises(ValueError, OrderItem, self.product, 0)
        self.assertRaises(TypeError, OrderItem, 'book', 1)

    # total price
    def test_calculate_total_price(self):
        self.assertEqual(self.order_one.total_price, 10)
        self.assertEqual(self.order_two.total_price, 20)

    # total tax
    def test_calculate_total_tax(self):
        self.assertEqual(self.order_one.total_tax, 1)
        self.assertEqual(self.order_two.total_tax, 2)

    # total amount
    def test_calculate_total_amount(self):
        self.assertEqual(self.order_one.total_amount, 11)
        self.assertEqual(self.order_two.total_amount, 22)


if __name__ == '__main__':
    unittest.main()
