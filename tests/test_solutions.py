import os
import time

import pandas as pd

import solutions

FIXTURES_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures')


class TestTask1:
    @classmethod
    def setup_class(cls):
        cls.__csv_sep = '|'
        fixtures_dir = f'{FIXTURES_DIRECTORY}/fetch_unique_entries_from_file'
        cls.__questions_answers = [
            {
                'src_fp': f'{fixtures_dir}/{subdir}/src.csv',
                'unique': pd.read_csv(f'{fixtures_dir}/{subdir}/unique.csv', sep=cls.__csv_sep),
                'duplicate_id_unique': pd.read_csv(
                    f'{fixtures_dir}/{subdir}/duplicate_id_unique.csv', sep=cls.__csv_sep),
            }
            for subdir in os.listdir(fixtures_dir)
        ]

    def test_fetch_unique_entries_from_file(self):
        for entry in self.__questions_answers:
            unique, duplicate_id_unique = solutions.fetch_unique_entries_from_file(entry['src_fp'], self.__csv_sep)
            assert unique.sort_values(by=list(unique.columns)).reset_index(drop=True).equals(
                entry['unique'].sort_values(by=list(entry['unique'].columns)).reset_index(drop=True)
            )
            assert (
                duplicate_id_unique
                .sort_values(by=list(duplicate_id_unique.columns))
                .reset_index(drop=True).equals(
                    entry['duplicate_id_unique']
                    .sort_values(by=list(entry['duplicate_id_unique'].columns))
                    .reset_index(drop=True))
            )


class TestTask2:
    @classmethod
    def setup_class(cls):
        cls.__float_precision = 0.0000000001
        cls.__questions_answers = [
            {
                'src': [{11, 3, 5}, {2, 17, 87, 32}, {4, 44}, {24, 11, 9, 7, 8}],
                'count': 14,
                'sum': 264,
                'mean': 18.8571428571,
                'tuple': (11, 3, 5, 2, 17, 87, 32, 4, 44, 24, 11, 9, 7, 8),
            },
        ]

    def test_count_all(self):
        for entry in self.__questions_answers:
            assert solutions.count_all(entry['src']) == entry['count']

    def test_sum_all(self):
        for entry in self.__questions_answers:
            assert solutions.sum_all(entry['src']) == entry['sum']

    def test_mean_all(self):
        for entry in self.__questions_answers:
            assert abs(solutions.mean_all(entry['src']) - entry['mean']) < self.__float_precision

    def test_tuple_all(self):
        for entry in self.__questions_answers:
            assert sorted(solutions.tuple_all(entry['src'])) == sorted(entry['tuple'])


class TestTask3:
    @classmethod
    def setup_class(cls):
        cls.__questions_answers = [
            {
                'src': [[1, 2, 3], [4, 5, 6]],
                'dicts': [{'k1': 1, 'k2': 2, 'k3': 3}, {'k1': 4, 'k2': 5, 'k3': 6}],
            },
        ]

    def test_lists2dicts(self):
        for entry in self.__questions_answers:
            assert solutions.lists2dicts(entry['src']) == entry['dicts']


class TestTask4:
    def test_remove_old_files(self, tmp_path):
        older_file_name = 'older.txt'
        newer_file_name = 'newer.txt'
        older_fp = f'{tmp_path}/{older_file_name}'
        newer_fp = f'{tmp_path}/{newer_file_name}'

        for max_days in [1, 2, 5, 10, 100]:
            assert os.listdir(tmp_path) == []

            for fp in [older_fp, newer_fp]:
                with open(fp, 'w'):
                    pass
            assert os.listdir(tmp_path) == [older_file_name, newer_file_name]

            control_time = time.time() - 60 * 60 * 24 * max_days
            os.utime(older_fp, (os.path.getatime(older_fp), control_time - 60))
            os.utime(newer_fp, (os.path.getatime(newer_fp), control_time + 60))

            solutions.remove_old_files(str(tmp_path), max_days)
            assert os.listdir(tmp_path) == [newer_file_name]

            for fp in [older_fp, newer_fp]:
                if os.path.exists(fp):
                    os.remove(fp)
            assert os.listdir(tmp_path) == []


class TestTask5:
    @classmethod
    def setup_class(cls):
        fixtures_dir = f'{FIXTURES_DIRECTORY}/join_words'
        cls.__questions_answers = []
        for subdir in os.listdir(fixtures_dir):
            entry = {'src_fp': f'{fixtures_dir}/{subdir}/words.txt'}
            with open(f'{fixtures_dir}/{subdir}/request_response.txt') as f:
                for line in f.readlines():
                    request, response = line.strip().split('|')
            entry.update({
                'request': request,
                'response': response.split(',')
            })
            cls.__questions_answers.append(entry)

    def test_lists2dicts(self):
        for entry in self.__questions_answers:
            assert sorted(solutions.join_words(entry['src_fp'], entry['request'])) == sorted(entry['response'])
