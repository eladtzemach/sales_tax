import unittest

from models.tax_rate import TaxRate


class TestTaxRate(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # create tax types
        # TaxRate(name, rate)
        cls.tax_exempt = TaxRate("TAX_EXEMPT", TaxRate.TAX_EXEMPT)
        cls.sales_tax = TaxRate("SALEX_TAX", TaxRate.SALES_TAX)
        cls.import_duty = TaxRate("IMPORT_DUTY", TaxRate.IMPORT_DUTY)

    @classmethod
    def tearDownClass(cls):
        pass

    # negative tax rate
    def test_constructor(self):
        self.assertRaises(ValueError, TaxRate, "TAX_TEST", -1)

    # tax exempt
    def test_calculate_tax_exempt(self):
        self.assertEqual(self.tax_exempt.calculate_tax(10), 0)

    # sales tax
    def test_calculate_tax_sales(self):
        self.assertEqual(self.sales_tax.calculate_tax(100), 10)

    # import duty
    def test_calculate_tax_import(self):
        self.assertEqual(self.import_duty.calculate_tax(500), 25)

if __name__ == '__main__':
    unittest.main()
