""" CustomList project. """
from itertools import zip_longest


class CustomList(list):
    """Main functions for Custom_list"""

    def __str__(self):
        """ Fuction for def print"""

        return f"Элементы списка: {[elem for elem in self]} \n " \
               f"Сумма элементов: {sum(self)}"

    def __add__(self, other):
        new_lst = [
            x + y for x, y in zip_longest(self, other, fillvalue=0)
        ]
        return CustomList(new_lst)

    def __iadd__(self, other):
        new_lst = [
            x + y for x, y in zip_longest(self, other, fillvalue=0)
        ]
        return CustomList(new_lst)

    def __radd__(self, other):
        new_lst = [
            x + y for x, y in zip_longest(self, other, fillvalue=0)
        ]
        return CustomList(new_lst)

    def __sub__(self, other):
        new_lst = [
            x - y for x, y in zip_longest(self, other, fillvalue=0)
        ]
        return CustomList(new_lst)

    def __isub__(self, other):
        new_lst = [
            x - y for x, y in zip_longest(self, other, fillvalue=0)
        ]
        return CustomList(new_lst)

    def __rsub__(self, other):
        new_lst = [
            x - y for x, y in zip_longest(other, self, fillvalue=0)
        ]
        return CustomList(new_lst)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)


if __name__ == '__main__':
    cust_list = CustomList([-5, -4, -3, -2, -1])
    main_list = [5, 6, 7]
    result_list_1 = cust_list - main_list
    result_list_2 = main_list - cust_list
    result_list_3 = cust_list + main_list
    result_list_4 = main_list + cust_list
    result_list_5 = cust_list + cust_list
    result_list_6 = cust_list - cust_list

    print(f"{cust_list}")
    print(f"{main_list}\n")
    print(
        f"{result_list_1}\n"
        f"{result_list_2}\n"
        f"{result_list_3}\n"
        f"{result_list_4}\n"
        f"{result_list_5}\n"
        f"{result_list_6}\n"
        f"{cust_list == cust_list}\n"
        f"{cust_list != cust_list}\n"
        f"{cust_list >= cust_list}\n"
        f"{main_list > cust_list}\n"
        f"{cust_list < main_list}\n"
    )

