from functions import *
import unittest

class TestSum(unittest.TestCase):

    def test_same_one(self):
        self.assertEqual(allTheSame(1,2,3), False, "Should be False")

    def test_same_two(self):
        self.assertEqual(allTheSame(1,1,1), True, "Should be True")

    def test_vowels_one(self):
        self.assertEqual(countVowels('homeostasis'),5,"Should be five")

    def test_vowels_two(self):
        self.assertEqual(countVowels('thermoplastic'),4,"Should be Four")

if __name__ == "__main__":
    unittest.main()
