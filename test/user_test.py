import unittest
import model.user as user


class UserTestCase(unittest.TestCase):

    def test_correct_login(self):
        result = user.login('test@gmail.com', 'password')
        self.assertEqual(result['ID'], 45)

    def test_wrong_password_login(self):
        result = user.login('test@gmail.com', 'password1')
        self.assertEqual(result, None)

    def test_wrong_email_login(self):
        result = user.login('test1@gmail.com', 'password')
        self.assertEqual(result, None)

    def test_correct_signup(self):
        result = user.signup('test1', 'test1', 'testcustomer1@gmail.com', 'password')
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
