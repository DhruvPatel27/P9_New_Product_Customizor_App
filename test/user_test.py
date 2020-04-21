import unittest

from model.user import login, signup


class UserTestCase(unittest.TestCase):
    def test_correct_login(self):
        result = login('leharcustomer@gmail.com', 'Password')
        correct_result = {'ID': 3, 'LastName': 'Bhatt', 'FirstName': 'Lehar', 'Email': 'leharcustomer@gmail.com',
                          'Password': 'Password', 'Role': 'Customer'}
        self.assertEqual(result, correct_result)

    def test_wrong_password_login(self):
        result = login('leharcustomer@gmail.com', 'Password1')
        correct_result = None
        self.assertEqual(result, correct_result)

    def test_wrong_email_login(self):
        result = login('lehar@gmail.com', 'Password')
        correct_result = None
        self.assertEqual(result, correct_result)

    def test_correct_signup(self):
        result = signup('test1', 'test1', 'testcustomer1@gmail.com', 'Password')
        correct_result = 1
        self.assertEqual(result, correct_result)


if __name__ == '__main__':
    unittest.main()
