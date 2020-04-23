import unittest
import model.order as order


class OrderTestCase(unittest.TestCase):

    def test_get_all_orders(self):
        result = order.get_all_orders()
        self.assertEqual(len(result), 1)

    def test_get_order_details_for_correct_user(self):
        result = order.get_order_details_for_user('test@gmail.com')
        self.assertEqual(len(result), 1)

    def test_get_order_details_for_incorrect_user(self):
        result = order.get_order_details_for_user('test1@gmail.com')
        self.assertEqual(len(result), 0)


if __name__ == '__main__':
    unittest.main()
