"""Test"""
import unittest
from main import CustomList


class MyTestCase(unittest.TestCase):
    """Test CustomList"""

    def test_str(self):
        """testing print custom list"""
        test_cl = CustomList([4, 1, 11, 10, 1])
        self.assertEqual(f"Элементы списка: {[elem for elem in test_cl]} \n " \
               f"Сумма элементов: {sum(test_cl)}",
                         test_cl.__str__())

    def test_getitem(self):
        """testing returning element from custom list"""
        test_cl = CustomList([4, 1, 11, 10, 1])
        self.assertEqual(11, test_cl[2])

    def test_eq(self):
        """testing == two custom lists"""
        test_cl_one = CustomList([1, 3, 4, 5, 123])
        test_cl_two = CustomList([3, 123, 4, 1, 5])
        self.assertTrue(test_cl_one == test_cl_two)
        test_cl_three = CustomList([3, 123, 4, 1, 50])
        self.assertFalse(test_cl_one == test_cl_three)
        test_cl_four = CustomList([3, 123, 4, 1, 5, 0])
        self.assertTrue(test_cl_one == test_cl_four)
        self.assertEqual([1, 3, 4, 5, 123], test_cl_one)

    def test_ne(self):
        """testing != two custom lists"""
        test_cl_one = CustomList([1, 3, 4, 5, 123])
        test_cl_two = CustomList([3, 123, 4, 1, 5])
        self.assertFalse(test_cl_one != test_cl_two)
        test_cl_three = CustomList([3, 123, 4, 1, 50])
        self.assertTrue(test_cl_one != test_cl_three)
        test_cl_four = CustomList([3, 123, 4, 1, 5, 0])
        self.assertFalse(test_cl_one != test_cl_four)
        self.assertEqual([1, 3, 4, 5, 123], test_cl_one)

    def test_lt(self):
        """testing < two custom lists"""
        test_cl_one = CustomList([2, 0, -4, 9, 13])
        test_cl_two = CustomList([0, 2, -4, 13, 9])
        self.assertFalse(test_cl_one < test_cl_two)
        test_cl_three = CustomList([3, 123, 4, 1, 50])
        self.assertTrue(test_cl_one < test_cl_three)
        self.assertFalse(test_cl_three < test_cl_one)
        test_cl_four = CustomList([1, 1, -2, 7, 13])
        self.assertFalse(test_cl_four < test_cl_one)
        self.assertFalse(test_cl_one < test_cl_four)
        self.assertEqual([2, 0, -4, 9, 13], test_cl_one)

    def test_le(self):
        """testing <= two custom lists"""
        test_cl_one = CustomList([2, 0, -4, 9, 13])
        test_cl_two = CustomList([0, 2, -4, 13, 9])
        self.assertTrue(test_cl_one <= test_cl_two)
        test_cl_three = CustomList([3, 123, 4, 1, 50])
        self.assertTrue(test_cl_one <= test_cl_three)
        self.assertFalse(test_cl_three <= test_cl_one)
        test_cl_four = CustomList([1, 1, -2, 7, 13])
        self.assertTrue(test_cl_four <= test_cl_one)
        self.assertTrue(test_cl_one <= test_cl_four)
        self.assertEqual([2, 0, -4, 9, 13], test_cl_one)

    def test_gt(self):
        """testing > two custom lists"""
        test_cl_one = CustomList([1, -8, 10, 9, 13])
        test_cl_two = CustomList([0, 2, -4, 13, 9])
        self.assertTrue(test_cl_one > test_cl_two)
        test_cl_three = CustomList([3, 123, 4, 1, 50])
        self.assertFalse(test_cl_one > test_cl_three)
        self.assertTrue(test_cl_three > test_cl_one)
        test_cl_four = CustomList([0, -10, 8, 11, 13])
        self.assertFalse(test_cl_four > test_cl_one)
        self.assertTrue(test_cl_one > test_cl_four)
        test_cl_five = CustomList([-8, 10, 1, 9, 13])
        self.assertFalse(test_cl_five > test_cl_one)
        self.assertFalse(test_cl_one > test_cl_five)
        self.assertEqual([1, -8, 10, 9, 13], test_cl_one)

    def test_ge(self):
        """testing >= two custom lists"""
        test_cl_one = CustomList([1, -8, 10, 9, 13])
        test_cl_two = CustomList([0, -7, 9, 13, 10])
        self.assertTrue(test_cl_one >= test_cl_two)
        test_cl_three = CustomList([3, 123, 4, 1, 50])
        self.assertFalse(test_cl_one >= test_cl_three)
        self.assertTrue(test_cl_three >= test_cl_one)
        test_cl_four = CustomList([0, -10, 8, 11, 13])
        self.assertFalse(test_cl_four >= test_cl_one)
        self.assertTrue(test_cl_one >= test_cl_four)
        test_cl_five = CustomList([-8, 10, 1, 9, 13])
        self.assertTrue(test_cl_five >= test_cl_one)
        self.assertTrue(test_cl_one >= test_cl_five)
        self.assertEqual([1, -8, 10, 9, 13], test_cl_one)

    def test_add(self):
        """testing custom list + custom list and custom list + list"""
        test_cl_one = CustomList([0, 1, 2, 3, 4])
        test_cl_two = CustomList([4, 3, 2, 1, 0])
        test_cl_three = CustomList([21, 54, 12])
        test_cl_four = [10, 11, 12, 13, 14]
        test_cl_five = [0, 1, 6]
        test_cl_six = []
        # Тест на сложение customlist одинаковой длины
        self.assertEqual([4, 4, 4, 4, 4], test_cl_one + test_cl_two)
        self.assertIsInstance((test_cl_one + test_cl_two), CustomList)
        # Tест на сложение customlist разной длины
        self.assertEqual([25, 57, 14, 1, 0], test_cl_three + test_cl_two)
        self.assertIsInstance((test_cl_three + test_cl_two), CustomList)
        # Тест на сложение customlist и list одинаковой длины
        self.assertEqual([10, 12, 14, 16, 18], test_cl_one + test_cl_four)
        self.assertIsInstance((test_cl_one + test_cl_four), CustomList)
        # Тест на сложение customlist и list разной длины
        self.assertEqual([0, 2, 8, 3, 4], test_cl_one + test_cl_five)
        self.assertIsInstance((test_cl_one + test_cl_five), CustomList)
        self.assertEqual([0, 1, 2, 3, 4], test_cl_one + test_cl_six)
        self.assertIsInstance((test_cl_one + test_cl_six), CustomList)
        # Проверка изменений в первоначальных списках
        self.assertEqual([0, 1, 2, 3, 4], test_cl_one)
        self.assertEqual([4, 3, 2, 1, 0], test_cl_two)
        self.assertEqual([21, 54, 12], test_cl_three)

    def test_iadd(self):
        """testing custom list + custom list and custom list + list"""
        test_cl_one = CustomList([0, 1, 2, 3, 4])
        test_cl_two = CustomList([4, 3, 2, 1, 0])
        test_cl_three = CustomList([21, 54, 12])
        test_cl_four = [10, 11, 12, 13, 14]
        test_cl_five = [0, 1, 6]
        test_cl_six = []
        test_cl_one += test_cl_two
        # Тест на сложение customlist одинаковой длины
        self.assertEqual([4, 4, 4, 4, 4], test_cl_one)
        self.assertIsInstance((test_cl_one), CustomList)
        # Tест на сложение customlist разной длины
        test_cl_one += test_cl_three
        self.assertEqual([25, 58, 16, 4, 4], test_cl_one)
        self.assertIsInstance((test_cl_one), CustomList)
        # Тест на сложение customlist и list одинаковой длины
        test_cl_one += test_cl_four
        self.assertEqual([35, 69, 28, 17, 18], test_cl_one)
        self.assertIsInstance((test_cl_one), CustomList)
        # Тест на сложение customlist и list разной длины
        test_cl_one += test_cl_five
        self.assertEqual([35, 70, 34, 17, 18], test_cl_one)
        self.assertIsInstance((test_cl_one), CustomList)
        test_cl_one += test_cl_six
        self.assertEqual([35, 70, 34, 17, 18], test_cl_one)
        self.assertIsInstance((test_cl_one), CustomList)
        # Проверка изменений в первоначальных списках
        self.assertEqual([4, 3, 2, 1, 0], test_cl_two)
        self.assertEqual([21, 54, 12], test_cl_three)

    def test_radd(self):
        """testing list + custom list"""
        test_cl_one = CustomList([0, 1, 2, 3, 4])
        test_cl_two = [3, 1, 8, 0, 10]
        test_cl_three = [3, 1, 8]
        test_cl_four = []
        self.assertEqual([3, 2, 10, 3, 14], test_cl_two + test_cl_one)
        self.assertIsInstance((test_cl_two + test_cl_one), CustomList)
        self.assertEqual([3, 2, 10, 3, 4], test_cl_three + test_cl_one)
        self.assertIsInstance((test_cl_three + test_cl_one), CustomList)
        self.assertEqual([0, 1, 2, 3, 4], test_cl_four + test_cl_one)
        self.assertIsInstance((test_cl_three + test_cl_one), CustomList)
        self.assertEqual([0, 1, 2, 3, 4], test_cl_one)

    def test_sub(self):
        """testing custom list - custom list and custom list - list"""
        test_cl_one = CustomList([0, 1, 2, 3, 4])
        test_cl_two = CustomList([4, 3, 2, 1, 0])
        test_cl_three = CustomList([21, 54, 12])
        test_cl_four = [10, 11, 12, 13, 14]
        test_cl_five = [0, 1, 6]
        test_cl_six = []
        test_cl_seven = CustomList([])
        # Тест на вычитание customlist одинаковой длины
        self.assertEqual([-4, -2, 0, 2, 4], test_cl_one - test_cl_two)
        self.assertIsInstance(test_cl_one - test_cl_two, CustomList)
        # Тест на вычитание customlist одинаковой длины
        self.assertEqual([4, 2, 0, -2, -4], test_cl_two - test_cl_one)
        self.assertIsInstance((test_cl_two - test_cl_one), CustomList)
        self.assertEqual([-17, -51, -10, 1, 0], test_cl_two - test_cl_three)
        # Тест на вычитание customlist разной длины
        self.assertIsInstance((test_cl_two - test_cl_one), CustomList)
        self.assertEqual([17, 51, 10, -1, 0], test_cl_three - test_cl_two)
        self.assertIsInstance((test_cl_three - test_cl_two), CustomList)
        # Тест на вычитание customlist и list одинаковой длины
        self.assertEqual([-10, -10, -10, -10, -10], test_cl_one - test_cl_four)
        self.assertIsInstance((test_cl_one - test_cl_four), CustomList)
        # Тест на вычитание customlist и list разной длины
        self.assertEqual([0, 0, -4, 3, 4], test_cl_one - test_cl_five)
        self.assertIsInstance((test_cl_one - test_cl_five), CustomList)
        self.assertEqual([0, -1, -6], test_cl_seven - test_cl_five)
        self.assertIsInstance((test_cl_seven - test_cl_five), CustomList)
        self.assertEqual([21, 54, 12], test_cl_three - test_cl_six)
        self.assertIsInstance((test_cl_three - test_cl_six), CustomList)
        # Проверка изменений в первоначальных списках
        self.assertEqual([0, 1, 2, 3, 4], test_cl_one)
        self.assertEqual([4, 3, 2, 1, 0], test_cl_two)
        self.assertEqual([21, 54, 12], test_cl_three)

    def test_isub(self):
        """testing custom list - custom list and custom list - list"""
        test_cl_one = CustomList([0, 1, 2, 3, 4])
        test_cl_two = CustomList([4, 3, 2, 1, 0])
        test_cl_three = CustomList([21, 54, 12])
        test_cl_four = [10, 11, 12, 13, 14]
        test_cl_five = [0, 1, 6]
        test_cl_six = []
        test_cl_seven = CustomList([])
        # Тест на вычитание customlist одинаковой длины
        test_cl_one -= test_cl_two
        self.assertEqual([-4, -2, 0, 2, 4], test_cl_one)
        self.assertIsInstance(test_cl_one, CustomList)
        # Тест на вычитание customlist разной длины
        test_cl_one -= test_cl_three
        self.assertIsInstance(test_cl_one, CustomList)
        self.assertEqual([-25, -56, -12, 2, 4], test_cl_one)
        # Тест на вычитание customlist и list одинаковой длины
        test_cl_one -= test_cl_four
        self.assertEqual([-35, -67, -24, -11, -10], test_cl_one)
        self.assertIsInstance(test_cl_one, CustomList)
        # Тест на вычитание customlist и list разной длины
        test_cl_one -= test_cl_five
        self.assertEqual([-35, -68, -30, -11, -10], test_cl_one)
        self.assertIsInstance(test_cl_one, CustomList)
        test_cl_one -= test_cl_six
        self.assertEqual([-35, -68, -30, -11, -10], test_cl_one)
        self.assertIsInstance(test_cl_one, CustomList)
        # Проверка изменений в первоначальных списках
        self.assertEqual([4, 3, 2, 1, 0], test_cl_two)
        self.assertEqual([21, 54, 12], test_cl_three)

    def test_rsub(self):
        """testing list - custom list"""
        test_cl_one = CustomList([0, 1, 2, 3, 4])
        test_cl_two = CustomList([4, 3, 2, 1, 0])
        test_cl_three = CustomList([21, 54, 12])
        test_cl_four = [0, 1, 6, 9, -10]
        test_cl_five = [1, 2, 3]
        test_cl_six = []
        test_cl_seven = CustomList([])
        # Тест на вычитание customlist и list одинаковой длины
        self.assertEqual([0, 0, 4, 6, -14], test_cl_four - test_cl_one)
        self.assertIsInstance((test_cl_four - test_cl_one), CustomList)
        # Тест на вычитание customlist и list разной длины
        self.assertEqual([-21, -53, -6, 9, -10], test_cl_four - test_cl_three)
        self.assertIsInstance((test_cl_four - test_cl_three), CustomList)
        self.assertEqual([-3, -1, 1, -1, 0], test_cl_five - test_cl_two)
        self.assertIsInstance((test_cl_five - test_cl_two), CustomList)
        self.assertEqual([], test_cl_six - test_cl_seven)
        self.assertIsInstance((test_cl_six - test_cl_seven), CustomList)
        # Проверка изменений в первоначальных списках
        self.assertEqual([0, 1, 2, 3, 4], test_cl_one)
        self.assertEqual([4, 3, 2, 1, 0], test_cl_two)
        self.assertEqual([21, 54, 12], test_cl_three)


if __name__ == '__main__':
    unittest.main()
