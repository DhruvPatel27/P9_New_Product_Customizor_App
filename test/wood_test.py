import unittest

import model.wood as wood


class WoodTestCase(unittest.TestCase):
    def test_wood_type(self):
        test_result = wood.get_wood()
        self.assertEqual(len(test_result), 5)

    def test_wood_design(self):
        test_result = wood.get_design()
        self.assertEqual(len(test_result), 6)

    def test_wood_type_by_id(self):
        test_result = wood.get_wood_by_id(1)
        self.assertEqual((test_result['name']), "Maple")

    def test_wood_type_by_wrong_id(self):
        test_result = wood.get_wood_by_id(999)
        self.assertEqual(test_result, None)

    def test_wood_design_by_id(self):
        test_result = wood.get_design_by_id(1)
        self.assertEqual(test_result['name'], "Bike")

    def test_wood_design_by_wrong_id(self):
        test_result = wood.get_design_by_id(999)
        self.assertEqual(test_result, None)


if __name__ == '__main__':
    unittest.main()
