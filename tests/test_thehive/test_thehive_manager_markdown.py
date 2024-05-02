import unittest

from sadif.frameworks_drivers.ticket_system.thehive.thehive_internal_mods_api.thehive_manager_markdown import (
    MarkdownConverter,
)


class TestMarkdownConverter(unittest.TestCase):
    def setUp(self):
        self.converter = MarkdownConverter()

    def test_convert_header(self):
        value = {"level": 2, "text": "Header Test"}
        expected_result = "## Header Test"
        assert self.converter.convert_header(value) == expected_result

    def test_convert_unordered_list(self):
        value = ["item1", "item2", "item3"]
        expected_result = "- item1\n- item2\n- item3"
        assert self.converter.convert_unordered_list(value) == expected_result

    def test_convert_ordered_list(self):
        value = ["item1", "item2", "item3"]
        expected_result = "1. item1\n2. item2\n3. item3"
        assert self.converter.convert_ordered_list(value) == expected_result

    def test_convert_fenced_code_block(self):
        value = "print('Hello, World!')"
        expected_result = "```\nprint('Hello, World!')\n```"
        assert self.converter.convert_fenced_code_block(value) == expected_result

    def test_convert_link(self):
        value = {"text": "Google", "url": "http://www.google.com"}
        expected_result = "[Google](http://www.google.com)"
        assert self.converter.convert_link(value) == expected_result

    def test_convert_image(self):
        value = {"alt_text": "Alt Text", "url": "http://www.example.com/image.jpg"}
        expected_result = "![Alt Text](http://www.example.com/image.jpg)"
        assert self.converter.convert_image(value) == expected_result

    def test_convert_table(self):
        value = {
            "headers": ["Header1", "Header2"],
            "rows": [["row1_col1", "row1_col2"], ["row2_col1", "row2_col2"]],
        }
        expected_result = "| Header1 | Header2 |\n| --- | --- |\n| row1_col1 | row1_col2 |\n| row2_col1 | row2_col2 |"
        assert self.converter.convert_table(value) == expected_result


if __name__ == "__main__":
    unittest.main()
