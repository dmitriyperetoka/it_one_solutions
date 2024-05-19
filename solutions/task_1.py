# Задание 1
# имеется текстовый файл f.csv, по формату похожий на .csv с разделителем |
"""
lastname|name|patronymic|date_of_birth|id
Фамилия1|Имя1|Отчество1 |21.11.1998   |312040348-3048
Фамилия2|Имя2|Отчество2 |11.01.1972   |457865234-3431
...
"""

# 1. Реализовать сбор уникальных записей
# 2. Случается, что под одинаковым id присутствуют разные данные - собрать такие записи

from typing import Tuple

import pandas as pd


def fetch_unique_entries_from_file(fp: str, csv_sep: str = '|') -> Tuple[pd.DataFrame, pd.DataFrame]:
    df = pd.read_csv(fp, sep=csv_sep)
    unique_entries = df.drop_duplicates()
    duplicate_id_unique_entries = unique_entries[unique_entries.duplicated('id', keep=False)]
    return unique_entries, duplicate_id_unique_entries
