""" filters in python"""


def is_even(n):
    """returns even number"""
    return n % 2 != 0


data = [1, 2, 3, 4, 5]
doubled = list(filter(is_even, data))
print(doubled)
