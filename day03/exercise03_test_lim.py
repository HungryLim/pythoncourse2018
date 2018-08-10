import unittest
<<<<<<< HEAD:day03/exercise03_test_lim.py
import os
os.chdir("C:/Users/wooki/Documents/GitHub/pythoncourse2018/day03")
from exercise03_lim import *
=======
from exercise03_erin import *
>>>>>>> upstream/master:day03/exercise03_test.py

class exerciseTests(unittest.TestCase):
    
    def test_vowels(self):
        self.assertEqual(4, count_vowels("mississippi"))
        with self.assertRaises(TypeError): count_vowels(5)
        with self.assertRaises(TypeError): count_vowels([1,2,3])

if __name__ == '__main__':
  unittest.main()

