# Задание 6*
# Имеется банковское API возвращающее JSON
# {
#     "Columns": ["key1", "key2", "key3"],
#     "Description": "Банковское API каких-то важных документов",
#     "RowCount": 2,
#     "Rows": [
#         ["value1", "value2", "value3"],
#         ["value4", "value5", "value6"]
#     ]
# }
# Основной интерес представляют значения полей "Columns" и "Rows",
# которые соответственно являются списком названий столбцов и значениями столбцов
# Необходимо:
#     1. Получить JSON из внешнего API
#         ендпоинт: GET https://api.gazprombank.ru/very/important/docs?documents_date={"начало дня сегодня в виде таймстемп"}
#         (!) ендпоинт выдуманный
#     2. Валидировать входящий JSON используя модель pydantic
#         (из ТЗ известно что поле "key1" имеет тип int, "key2"(datetime), "key3"(str))
#     2. Представить данные "Columns" и "Rows" в виде плоского csv-подобного pandas.DataFrame
#     3. В полученном DataFrame произвести переименование полей по след. маппингу
#         "key1" -> "document_id", "key2" -> "document_dt", "key3" -> "document_name"
#     3. Полученный DataFrame обогатить доп. столбцом:
#         "load_dt" -> значение "сейчас"(датавремя)
# *реализовать п.1 с использованием Apache Airflow HttpHook

import datetime
from typing import Optional

import pandas as pd
from airflow.providers.http.hooks.http import HttpHook
from pydantic import BaseModel


def extract_transform_data(
        endpoint: str,
        http_conn_id: str = 'http_default',
        datetime_format: Optional[str] = None,
) -> pd.DataFrame:
    class BankDoc(BaseModel):
        key1: int
        key2: datetime.datetime
        key3: str

    http_hook = HttpHook(method='GET', http_conn_id=http_conn_id)
    data = http_hook.run(endpoint).json()

    columns = data['Columns']
    rows = data['Rows']

    for row in rows:
        BankDoc.model_validate({key: value for key, value in zip(columns, row)})

    datetime_now = datetime.datetime.now()
    df = (
        pd.DataFrame(data=rows, columns=columns)
        .rename(columns={'key1': 'document_id', 'key2': 'document_dt', 'key3': 'document_name'})
        .assign(**{'load_dt': [datetime_now] * len(rows)})
    )
    df['document_dt'] = pd.to_datetime(df['document_dt'], format=datetime_format)

    return df
