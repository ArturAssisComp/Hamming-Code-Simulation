from tools import comparator
import unittest


class TestTools(unittest.TestCase):

    def test_comparator(self):
        with self.assertRaises(ValueError):
            comparator([1, 0], [1, 1, 0])
        self.assertEqual(comparator([1, 0, 0, 1, 1], [1, 0, 1, 1, 0]), 0.4)
        self.assertEqual(comparator([0, 0, 0], [1, 1, 1]), 1)
        self.assertEqual(comparator([1], [1]), 0)


if __name__ == '__main__':
    unittest.main()
