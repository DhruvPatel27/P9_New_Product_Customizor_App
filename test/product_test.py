import unittest
from unittest.mock import patch
from model.product import get_products

class ProductTestCase(unittest.TestCase):

    @patch('model.product.db_connection')
    def test_get_products(self,mock_conn):
        r = get_products()
        mock_conn.get_connection.assert_called_once()

if __name__ == '__main__':
    unittest.main()

