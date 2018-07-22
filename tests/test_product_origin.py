import unittest

from models.product_origin import ProductOrigin
from models.tax_rate import TaxRate


class TestProductOrigin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create tax types
        # TaxRate(name, rate)
        tax_exempt = TaxRate("TAX_EXEMPT", TaxRate.TAX_EXEMPT)
        import_duty = TaxRate("IMPORT_DUTY", TaxRate.IMPORT_DUTY)

        # create the additional local/imported tax types
        # ProductOrigin(name, TaxRate)
        cls.local = ProductOrigin(ProductOrigin.LOCAL, tax_exempt)
        cls.imported = ProductOrigin(ProductOrigin.IMPORTED, import_duty)

    @classmethod
    def tearDownClass(cls):
        pass

    # invalid tax rate
    def test_constructor(self):
        self.assertRaises(TypeError, ProductOrigin, 'test', 'rate')

    # tax for local
    def test_calculate_tax_local(self):
        self.assertEqual(self.local.calculate_tax(10), 0)

    # tax for imported
    def test_calculate_tax_imported(self):
        self.assertEqual(self.imported.calculate_tax(10), 0.5)


if __name__ == '__main__':
    unittest.main()
