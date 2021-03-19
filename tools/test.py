from tools import comparator, get_minimum_error, decoder
import unittest
import numpy as np


class TestTools(unittest.TestCase):

    def test_comparator(self):
        with self.assertRaises(ValueError):
            comparator([1, 0], [1, 1, 0])
        self.assertEqual(comparator([1, 0, 0, 1, 1], [1, 0, 1, 1, 0]), 0.4)
        self.assertEqual(comparator([0, 0, 0], [1, 1, 1]), 1)
        self.assertEqual(comparator([1], [1]), 0)

    def test_minimum_error(self):
        self.assertTrue(np.array_equal(get_minimum_error([1, 1, 0]), [0, 0, 1, 0, 0, 0, 0]))

    def test_decoder(self):
        self.assertTrue(np.array_equal(decoder([0,0, 1, 0, 0, 0, 0]), [0, 0, 0, 0]))

if __name__ == '__main__':
    unittest.main()
