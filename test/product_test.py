import unittest
from unittest.mock import patch
import model.product as product

class ProductTestCase(unittest.TestCase):

    # def setUp(self):
    #     self.test_product['title']="TestProduct"
    #     self.test_product['description']="TestProduct"
    #     self.test_product['price']="TestProduct"
    #     self.test_product['category']="TestProduct"
    #     self.test_product['occasion']="TestProduct"
    #     self.test_product['image']="TestProduct"
    #     self.test_product['model_id']= 1

    # def tearDown(self):
    #     self.test_product.dispose()


    def test_get_products(self):
        test_products = product.get_products()
        self.assertEqual(len(test_products), 4)
    
    def test_get_product_details_correct_id(self):
        test_products = product.get_product_details(1)
        self.assertEqual(test_products['title'], 'Engraved Wood Coaster')

    def test_get_product_details_incorrect_id(self):
        test_products = product.get_product_details(20)
        self.assertEqual(test_products, None)

    def test_get_product_by_occasion(self):
        test_products = product.get_products_by_occasion("Valentines Day")
        self.assertEqual(len(test_products), 3)

    def test_get_product_by_category(self):
        test_products = product.get_products_by_category("Coaster")
        self.assertEqual(len(test_products), 4)

    def test_get_product_by_occasion_incorrect(self):
        test_products = product.get_products_by_occasion("Easter")
        self.assertEqual(len(test_products), 0)

    def test_get_product_by_category_incorrect(self):
        test_products = product.get_products_by_category("Chopping Board")
        self.assertEqual(len(test_products), 0)
    
    def test_search_product_by_name(self):
        test_products = product.search_product_by_name("Engraved Wood Coaster")
        self.assertEqual(len(test_products), 1)

    def test_search_product_by_name_incorrect(self):
        test_products = product.search_product_by_name("Engraved Wood Coaster 3")
        self.assertEqual(len(test_products), 0)
    
    def test_get_products_mask(self):
        test_products = product.get_products_mask(1)
        self.assertEqual(len(test_products), 1)

    def test_get_products_mask_incorrect(self):
        test_products = product.get_products_mask(89)
        self.assertEqual(len(test_products), 0)

    def test_get_product_details_cart(self):
        test_products = product.get_product_details_cart(1)
        self.assertEqual(len(test_products), 3)
        self.assertEqual(test_products['title'], 'Engraved Wood Coaster')
        self.assertEqual(test_products['price'], 25.49)
        self.assertEqual(test_products['Product_id'], 1)

    def test_get_product_details_cart_incorrect(self):
        test_products = product.get_product_details_cart(89)
        self.assertEqual(test_products, None)

if __name__ == '__main__':
    unittest.main()

