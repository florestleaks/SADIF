import unittest
from unittest.mock import patch

from sadif.utils.generate_string.random_string_generator import RandomStringGenerator


class TestRandomStringGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = RandomStringGenerator()

    @patch("sadif.utils.generate_string.random_string_generator.random.choices")
    @patch("sadif.utils.generate_string.random_string_generator.random.randint")
    def test_generate_string_title(self, mock_randint, mock_choices):
        mock_randint.return_value = 10
        mock_choices.return_value = ["a"] * 10
        title = self.generator.generate_string_title("example")
        self.assertEqual(title, "test de example - aaaaaaaaaa")

    @patch("sadif.utils.generate_string.random_string_generator.random.choices")
    @patch("sadif.utils.generate_string.random_string_generator.random.randint")
    def test_generate_string_paragraph(self, mock_randint, mock_choices):
        mock_randint.return_value = 5
        mock_choices.return_value = ["b"] * 5
        paragraph = self.generator.generate_string_paragraph(3)
        expected_output = "bbbbb bbbbb bbbbb"
        self.assertEqual(paragraph, expected_output)

    def test_generate_string_paragraph_with_non_integer(self):
        with self.assertRaises(ValueError):
            self.generator.generate_string_paragraph(-1)

    def test_generate_string_paragraph_with_negative_number(self):
        with self.assertRaises(ValueError):
            self.generator.generate_string_paragraph(-1)

    # Aqui você pode adicionar mais testes conforme necessário


if __name__ == "__main__":
    unittest.main()
