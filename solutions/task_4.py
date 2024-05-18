import os
import time

# Задание 4
# Имеется папка с файлами
# Реализовать удаление файлов старше N дней


def remove_old_files(dir_: str, max_days: int) -> None:
    control_time = time.time() - 60 * 60 * 24 * max_days
    for file_name in os.listdir(dir_):
        fp = f'{dir_}/{file_name}'
        if os.path.getmtime(fp) < control_time:
            os.remove(fp)
