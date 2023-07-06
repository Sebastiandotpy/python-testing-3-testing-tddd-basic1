import unittest
from text import to_upper, to_word_list_isupper

class TestToUpper(unittest.TestCase):
    def test_to_upper(self):
        result = to_upper("abcdef")
        self.assertEqual(result, "ABCDEF")

    def test_to_upper_with_non_string(self):
        with self.assertRaises(TypeError):
            to_upper(123)

class TestToWordListIsUpper(unittest.TestCase):
    def test_to_word_list_isupper(self):
        result = to_word_list_isupper(['I', 'LOVE', 'YOU'])
        self.assertTrue(result)

    def test_to_word_list_isupper_with_non_list(self):
        with self.assertRaises(TypeError):
            to_word_list_isupper("Hello")

    def test_to_word_list_isupper_with_mixed_case(self):
        result = to_word_list_isupper(['I', 'LoVe', 'YOu'])
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
