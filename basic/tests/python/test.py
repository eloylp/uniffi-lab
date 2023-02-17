import unittest
from basic import *

class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(6, add(2, 4))
    def test_add_errors_overflow(self):
        with self.assertRaises(ArithmeticError.IntegerOverflow) as context:
            add(4294967295, 1)
        self.assertEquals(4294967295, context.exception.a)
        self.assertEquals(1, context.exception.b)

if __name__ == '__main__':
    unittest.main()
