import unittest

from models.product import Product
from models.product_category import ProductCategory
from models.product_origin import ProductOrigin
from models.tax_rate import TaxRate


class TestProduct(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create tax types
        # TaxRate(name, rate)
        tax_exempt = TaxRate("TAX_EXEMPT", TaxRate.TAX_EXEMPT)
        sales_tax = TaxRate("SALEX_TAX", TaxRate.SALES_TAX)
        import_duty = TaxRate("IMPORT_DUTY", TaxRate.IMPORT_DUTY)

        # create item categories
        # ProductCategory(name, TaxRate)
        cls.books = ProductCategory(ProductCategory.BOOKS, tax_exempt)
        cls.other = ProductCategory(ProductCategory.OTHER, sales_tax)

        # create the additional local/imported tax types
        # ProductOrigin(name, TaxRate)
        cls.local = ProductOrigin(ProductOrigin.LOCAL, tax_exempt)
        cls.imported = ProductOrigin(ProductOrigin.IMPORTED, import_duty)

    @classmethod
    def tearDownClass(cls):
        pass

    # negative price for product, invalid category, invalid origin
    def test_constructor(self):
        self.assertRaises(ValueError, Product, 'book', self.books, self.local, -1)
        self.assertRaises(TypeError, Product, 'book', 'category', self.local, 1)
        self.assertRaises(TypeError, Product, 'book', self.books, 'origin', 1)

    # tax for product
    def test_calculate_tax_local_pass(self):
        product = Product("music CD", self.other, self.local, 10)
        self.assertEqual(product.calculate_tax(), 1.0)

    def test_calculate_tax_local_fail(self):
        product = Product("music CD", self.other, self.local, 10)
        self.assertNotEqual(product.calculate_tax(), 0.05)

    def test_calculate_tax_imported_fail(self):
        product = Product("music CD", self.other, self.imported, 10)
        self.assertNotEqual(product.calculate_tax(), 1.0)

    def test_calculate_tax_imported_pass(self):
        product = Product("music CD", self.other, self.imported, 10)
        self.assertEqual(product.calculate_tax(), 1.5)

if __name__ == '__main__':
    unittest.main()
