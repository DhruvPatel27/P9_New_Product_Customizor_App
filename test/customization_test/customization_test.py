import unittest
import base64

from io import BytesIO
from PIL import Image
from model.customization import show_preview, show_default_preview


class CustomizationTestCase(unittest.TestCase):
    def test_wood_default(self):
        result = show_default_preview(1, 1)
        known_result = Image.open("wood.png")
        img = BytesIO()
        known_result.save(img, format='PNG')
        img = img.getvalue()
        known_result = base64.b64encode(img)

        self.assertEqual(result, known_result)

    def test_wood(self):
        result = show_preview(1, 1, 6, "")
        known_result = Image.open("wood.png")
        img = BytesIO()
        known_result.save(img, format='PNG')
        img = img.getvalue()
        known_result = base64.b64encode(img)

        self.assertEqual(result, known_result)

    def test_wood_text(self):
        result = show_preview(1, 1, 6, "Hello")
        known_result = Image.open("wood_text.png")
        img = BytesIO()
        known_result.save(img, format='PNG')
        img = img.getvalue()
        known_result = base64.b64encode(img)

        self.assertEqual(result, known_result)

    def test_wood_design(self):
        result = show_preview(1, 1, 1, "")
        known_result = Image.open("wood_design.png")
        img = BytesIO()
        known_result.save(img, format='PNG')
        img = img.getvalue()
        known_result = base64.b64encode(img)

        self.assertEqual(result, known_result)

    def test_wood_design_text(self):
        result = show_preview(1, 1, 1, "Hello")
        known_result = Image.open("wood_design_text.png")
        img = BytesIO()
        known_result.save(img, format='PNG')
        img = img.getvalue()
        known_result = base64.b64encode(img)

        self.assertEqual(result, known_result)

if __name__ == '__main__':
    unittest.main()