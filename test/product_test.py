import unittest
from unittest.mock import patch
import model.product as product

class ProductTestCase(unittest.TestCase):

    def test_get_products(self):
        test_products = product.get_products()
        self.assertEqual(len(test_products), 4)
    
    def test_get_product_details_correct_id(self):
        test_products = product.get_product_details(1)
        self.assertEqual(test_products['title'], 'Engraved Wood Coaster')

    def test_get_product_details_incorrect_id(self):
        test_products = product.get_product_details(20)
        self.assertEqual(test_products, None)
    


if __name__ == '__main__':
    unittest.main()

