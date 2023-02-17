import unittest
from basic import *

class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(6, add(2, 4))

if __name__ == '__main__':
    unittest.main()
