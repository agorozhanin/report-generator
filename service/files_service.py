"""Модуль для работы с файлами"""
import os
from datetime import datetime

PATH_TO_TASKS_FOLDER = 'tasks'


def create_tasks_directory_if_needed() -> None:
    """Создаёт папку tasks, если это необходимо"""
    if not os.path.isdir(PATH_TO_TASKS_FOLDER):
        os.mkdir(PATH_TO_TASKS_FOLDER)


def create_and_write_txt_file_by_name(filename: str, data_to_write) -> None:
    """Создаёт текстовый файл с необходимым именем.

    Записывает в него необходимую информацию.
    В случае существования такого файла старый файл переименовывается.
    Название обновлённого файла представляется в формате:
    "old_<имя файла>_год-месяц-числоTчасы-минуты".
    Выполнение данной функции производится не более раза в минуту.

    """
    full_filename = "".join([filename, '.txt'])
    path_to_file = "/".join([PATH_TO_TASKS_FOLDER, full_filename])
    if os.path.exists(path_to_file):
        current_datetime = datetime.now().strftime("%Y-%m-%dT%H-%M")
        new_filename_for_old_file = "_".join(['old', filename, current_datetime])
        new_full_filename_for_old_file = "".join([new_filename_for_old_file, '.txt'])
        path_to_rename_file = "/".join([PATH_TO_TASKS_FOLDER, new_full_filename_for_old_file])
        try:
            os.rename(path_to_file, path_to_rename_file)
        except FileExistsError:
            pass

    with open(file=path_to_file, mode='w+', encoding='utf-8') as new_file:
        new_file.write(data_to_write)
