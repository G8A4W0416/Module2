import unittest
from main import camper_age_input


class FunctionTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(36, camper_age_input.convert_to_months(3))


if __name__ == '__main__':
    unittest.main()
