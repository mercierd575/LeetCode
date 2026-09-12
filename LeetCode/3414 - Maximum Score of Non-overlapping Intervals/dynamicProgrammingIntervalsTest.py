import unittest
from dynamicProgrammingIntervals import maximumWeight

class MyTestCase(unittest.TestCase):
    def test1(self):
        input1 = [
            [1, 3, 2],
            [4, 5, 2],
            [1, 5, 5],
            [6, 9, 3],
            [6, 7, 1],
            [8, 9, 1]
        ]
        expected_out1 = [2, 3]

        self.assertEqual(expected_out1, maximumWeight(input1))

    def test2(self):
        input2 = [
            [5, 8, 1],
            [6, 7, 7],
            [4, 7, 3],
            [9, 10, 6],
            [7, 8, 2],
            [11, 14, 3],
            [3, 5, 5]
        ]
        expected_out2 = [1, 3, 5, 6]

        self.assertEqual(expected_out2, maximumWeight(input2))

if __name__ == '__main__':
    unittest.main()
