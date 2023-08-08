import json
import os, sys
import unittest
from unittest.mock import patch, mock_open
sys.path.append(os.path.abspath(os.path.join("../parse_json/")))
from scripts import sniffer


class SnifferTestCase(unittest.TestCase):

    def setUp(self):
        self.sniffer = sniffer.Sniffer()
        self.test_data_dir = "./tests/data"
        self.test_output_dir = "./tests/schema"

    def tearDown(self):
        # Clean up test output directory after each test
        # for file in os.listdir(self.test_output_dir):
        #     file_path = os.path.join(self.test_output_dir, file)
        #     os.remove(file_path)
        pass

    def test_sniff_schema_with_valid_data(self):
        # Prepare test data
        json_input = {
            "message": {
                "key_one": "value_one",
                "key_two": 123,
                "key_three": ["value_one", "value_two"]
            }
        }

        # Expected output schema
        expected_schema = {
            "key_one": {
                "type": "string",
                "tag": "",
                "description": "",
                "required": False
            },
            "key_two": {
                "type": "integer",
                "tag": "",
                "description": "",
                "required": False
            },
            "key_three": {
                "type": "enum",
                "tag": "",
                "description": "",
                "required": False
            }
        }

        # Call sniff_schema method and assert the output
        output_schema = self.sniffer.sniff_schema(json_input)
        self.assertEqual(output_schema, expected_schema)


if __name__ == "__main__":
    unittest.main()
