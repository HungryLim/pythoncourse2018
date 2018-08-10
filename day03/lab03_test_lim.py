import unittest
from lab03 import *

class labTests(unittest.TestCase):
	
	## fill in a few tests for each
	## make sure to account for correct and incorrect input

    def test_shout(self):
        self.assertEqual(4, test_shout("mississippi"))
        with self.assertRaises(TypeError): test_shout(5)
        with self.assertRaises(TypeError): test_shout([1,2,3])

    def test_reverse(self):

    def test_reversewords(self):

    def test_reversewordletters(self):

    def test_piglatin(self):


if __name__ == '__main__':
  unittest.main()

