# Задание 2
# в наличии список множеств. внутри множества целые числа
# посчитать 
#  1. общее количество чисел
#  2. общую сумму чисел
#  3. посчитать среднее значение
#  4. собрать все числа из множеств в один кортеж
"""
m = [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}]
"""
# *написать решения в одну строку

import statistics
from typing import List, Set, Tuple


def count_all(src: List[Set[int]]) -> int:
    """общее количество чисел"""
    return sum(len(x) for x in src)


def sum_all(src: List[Set[int]]) -> int:
    """общую сумму чисел"""
    return sum(sum(x) for x in src)


def mean_all(src: List[Set[int]]) -> float:
    """посчитать среднее значение"""
    return statistics.mean((elem for set_ in src for elem in set_))


def tuple_all(src: List[Set[int]]) -> Tuple[int, ...]:
    """собрать все числа из множеств в один кортеж"""
    return tuple(elem for set_ in src for elem in set_)
