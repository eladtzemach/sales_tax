import unittest

from models.product_category import ProductCategory
from models.tax_rate import TaxRate


class TestProductCategory(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create tax types
        # TaxRate(name, rate)
        tax_exempt = TaxRate("TAX_EXEMPT", TaxRate.TAX_EXEMPT)
        sales_tax = TaxRate("SALEX_TAX", TaxRate.SALES_TAX)

        # create item categories
        # ProductCategory(name, TaxRate)
        cls.books = ProductCategory(ProductCategory.BOOKS, tax_exempt)
        cls.food = ProductCategory(ProductCategory.FOOD, tax_exempt)
        cls.medical = ProductCategory(ProductCategory.MEDICAL, tax_exempt)
        cls.other = ProductCategory(ProductCategory.OTHER, sales_tax)

    @classmethod
    def tearDownClass(cls):
        pass

    # invalid tax rate
    def test_constructor(self):
        self.assertRaises(TypeError, ProductCategory, ProductCategory.BOOKS, 'tax')

    # tax for books
    def test_calculate_tax_books(self):
        self.assertEqual(self.books.calculate_tax(10), 0)

    # tax for food
    def test_calculate_tax_food(self):
        self.assertEqual(self.food.calculate_tax(10), 0)

    # tax for medical
    def test_calculate_tax_medical(self):
        self.assertEqual(self.medical.calculate_tax(10), 0)

    # tax for other
    def test_calculate_tax_other(self):
        self.assertEqual(self.other.calculate_tax(10), 1.0)


if __name__ == '__main__':
    unittest.main()
