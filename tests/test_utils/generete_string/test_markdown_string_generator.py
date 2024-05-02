import unittest
from unittest.mock import patch

from sadif.utils.generete_string.markdown_string_generator import MarkdownStringGenerator


class TestMarkdownStringGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = MarkdownStringGenerator()

    @patch("sadif.utils.generete_string.markdown_string_generator.random.choices")
    def test_generate_title(self, mock_choices):
        mock_choices.return_value = ["a"] * 10
        title = self.generator.generate_title(1)
        self.assertEqual(title, "# aaaaaaaaaa")

    @patch("sadif.utils.generete_string.markdown_string_generator.random.choices")
    def test_generate_list(self, mock_choices):
        mock_choices.return_value = ["b"] * 10
        list_md = self.generator.generate_list(3)
        expected_output = "- bbbbbbbbbb\n- bbbbbbbbbb\n- bbbbbbbbbb"
        self.assertEqual(list_md, expected_output)

    @patch("sadif.utils.generete_string.markdown_string_generator.random.choices")
    def test_generate_code_block(self, mock_choices):
        mock_choices.return_value = ["c"] * 15
        code_block = self.generator.generate_code_block(2)
        expected_output = "```\nccccccccccccccc\nccccccccccccccc\n```"
        self.assertEqual(code_block, expected_output)

    @patch("sadif.utils.generete_string.markdown_string_generator.random.choices")
    def test_generate_paragraph(self, mock_choices):
        mock_choices.return_value = ["d"] * 8
        paragraph = self.generator.generate_paragraph(4)
        expected_output = "dddddddd dddddddd dddddddd dddddddd"
        self.assertEqual(paragraph, expected_output)

    # Aqui você pode adicionar mais testes conforme necessário


if __name__ == "__main__":
    unittest.main()
