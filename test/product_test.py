import model.product as product
import unittest

class ProductTestCase(unittest.TestCase):
    def test_get_products(self):
        result = product.get_products()
        self.assertIsNotNone(result)

    def test_get_product_details(self):
        result = product.get_product_details(11)
        self.assertEqual(len(result), 8)

    def test_get_product_by_occasion(self):
        result = product.get_products_by_occasion("Graduation")
        self.assertAlmostEqual(result['occasion'], "Graduation")

    def test_get_product_by_category(self):
        result = product.get_products_by_category("Phone")
        self.assertEqual(result['category'], "Phone")

    def test_get_products_mask(self):
        result = product.get_products_mask(17)
        self.assertIsNotNone(result)

    def test_get_product_details_cart(self):
        result = product.get_product_details_cart(11)
        self.assertIsNotNone(result)

    def test_search_product_by_name(self):
        result = product.search_product_by_name("iPhone XS Wood Case")
        self.assertEqual(result['title'], "iPhone XS Wood Case")