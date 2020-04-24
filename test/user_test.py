import unittest
import model.user as user
import model.db_connection as db_connection


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

    def tearDown_for_signup(self, user_id):
        connection = db_connection.get_connection()
        with connection.cursor() as cursor:
            sql = "DELETE from USER where `ID`=%s"
            cursor.execute(sql, user_id)
            connection.commit()

    def test_correct_signup(self):
        result, user_id = user.signup('test1', 'test1', 'testcustomer1@gmail.com', 'password')
        self.assertEqual(result, 1)
        self.tearDown_for_signup(user_id)


if __name__ == '__main__':
    unittest.main()
