import unittest

from models.receipt import Receipt


class TestReceipt(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    # pass an empty list
    def test_constructor(self):
        self.assertRaises(ValueError, Receipt, [])

if __name__ == '__main__':
    unittest.main()
