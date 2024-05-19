# Задание 3
# имеется список списков
# a = [[1,2,3], [4,5,6]]
# сделать список словарей
# b = [{'k1': 1, 'k2': 2, 'k3': 3}, {'k1': 4, 'k2': 5, 'k3': 6}]
# *написать решение в одну строку

from typing import List, Dict


def lists2dicts(src: List[List[int]]) -> List[Dict[str, int]]:
    return [{f'k{ind}': elem for ind, elem in enumerate(sublist, 1)} for sublist in src]
