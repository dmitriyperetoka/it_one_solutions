# Задание 5*
"""
Имеется текстовый файл с набором русских слов(имена существительные, им.падеж)
Одна строка файла содержит одно слово.
Написать программу которая выводит список слов, каждый элемент списка которого - это новое слово,
которое состоит из двух сцепленных в одно, которые имеются в текстовом файле.
Порядок вывода слов НЕ имеет значения
Например, текстовый файл содержит слова: ласты, стык, стыковка, баласт, кабала, карась
Пользователь вводмт первое слово: ласты
Программа выводит:
ластык
ластыковка
Пользователь вводмт первое слово: кабала
Программа выводит:
кабаласты
кабаласт
Пользователь вводмт первое слово: стыковка
Программа выводит:
стыковкабала
стыковкарась
"""

from typing import List


def join_words(fp: str, first_word: str) -> List[str]:
    with open(fp) as f:
        src_words = [line.strip() for line in f.readlines()]

    result_words = []
    for src_word in src_words:
        if first_word != src_word:
            cursor = min(len(first_word), len(src_word))
            while cursor >= 0:
                if first_word[-1 - cursor:] == src_word[:cursor + 1]:
                    result_words.append(first_word + src_word[cursor + 1:])
                    break
                cursor -= 1

    return result_words
