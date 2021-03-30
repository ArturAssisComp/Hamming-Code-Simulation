import tools as tl
import unittest
import numpy as np


class TestTools(unittest.TestCase):

    def test_comparator(self):
        with self.assertRaises(ValueError):
            tl.comparator([1, 0], [1, 1, 0])
        self.assertEqual(tl.comparator([1, 0, 0, 1, 1], [1, 0, 1, 1, 0]), 2)
        self.assertEqual(tl.comparator([0, 0, 0], [1, 1, 1]), 3)
        self.assertEqual(tl.comparator([1], [1]), 0)

    def test_minimum_error(self):
        self.assertTrue(np.array_equal(
            tl.get_minimum_error([1, 1, 0]), [0, 0, 1, 0, 0, 0, 0]))

    def test_decoder(self):
        self.assertTrue(np.array_equal(tl.decoder(
            [0, 0, 1, 0, 0, 0, 0]), [0, 0, 0, 0]))


if __name__ == '__main__':
    unittest.main()
