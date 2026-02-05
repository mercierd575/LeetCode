import unittest
from FastPow import myPow


class FastPowTest(unittest.TestCase):

    def test_1(self):
        x = 2.00000
        n = 10

        actual = myPow(x, n)
        expected = 1024.00000

        self.assertEqual(actual, expected)

    def test_2(self):
        x = 2.10000
        n = 3

        actual = myPow(x, n)
        expected = 9.26100

        self.assertAlmostEqual(actual, expected, places=5)

    def test_3(self):
        x = 2.00000
        n = -2

        actual = myPow(x, n)
        expected = 0.25

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
