import unittest
from peak_finder import PeakFinder


class PeakFinderTest(unittest.TestCase):

    def test_1d_straightforward_algorithm(self):
        finder = PeakFinder()
        self.assertEqual(5, finder.one_dimensional_straightforward_find([1,2,3,4,5]))
        self.assertEqual(5, finder.one_dimensional_straightforward_find([5,4,3,2,1]))
        self.assertEqual(7, finder.one_dimensional_straightforward_find([6,7,4,3,2,1,5,4]))

    def test_1d_divide_and_conquer_algorithm(self):
        finder = PeakFinder()
        self.assertEqual(5, finder.one_dimensional_straightforward_find([1,2,3,4,5]))
        self.assertEqual(5, finder.one_dimensional_straightforward_find([5,4,3,2,1]))
        self.assertEqual(7, finder.one_dimensional_straightforward_find([6,7,4,3,2,1,5,4]))

    def test_2d_straightforward_algorithm(self):
        finder = PeakFinder()
        self.assertEqual(16, finder.two_dimensional_straightforward_find([
            [ 1, 2, 3, 4],
            [ 5, 6, 7, 8],
            [ 9,10,11,12],
            [13,14,15,16]
        ]))
        self.assertEqual(16, finder.two_dimensional_straightforward_find([
            [16, 15, 14, 13],
            [12, 11, 10,  9],
            [ 8,  7,  6,  5],
            [ 4,  3,  2,  1]
        ]))
        self.assertEqual(6, finder.two_dimensional_straightforward_find([
            [1,3,5,4],
            [2,4,6,5],
            [3,2,4,1],
            [3,4,2,1]
        ]))

    def test_2d_divide_and_conquer_algorithm(self):
        finder = PeakFinder()
        self.assertEqual(16, finder.two_dimensional_divide_and_conquer_find([
            [ 1, 2, 3, 4],
            [ 5, 6, 7, 8],
            [ 9,10,11,12],
            [13,14,15,16]
        ]))
        self.assertEqual(16, finder.two_dimensional_divide_and_conquer_find([
            [16, 15, 14, 13],
            [12, 11, 10,  9],
            [ 8,  7,  6,  5],
            [ 4,  3,  2,  1]
        ]))
        self.assertEqual(6, finder.two_dimensional_straightforward_find([
            [1,3,5,4],
            [2,4,6,5],
            [3,2,4,1],
            [3,4,2,1]
        ]))


if __name__ == '__main__':
    unittest.main()
