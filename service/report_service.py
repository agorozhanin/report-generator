"""Модуль для формирования отчётов"""
import string
from datetime import datetime

from service.api_service import get_tasks_list_from_api
from service.files_service import create_and_write_txt_file_by_name


def create_reports(users_list: list) -> None:
    """Создаёт отчёты для всех необходимых пользователей"""
    all_tasks_list = get_tasks_list_from_api()

    with open('report_template.tpl', encoding='utf-8') as tpl:
        temp = tpl.read()
    template = string.Template(temp)

    dict_to_template = dict()
    for user in users_list:
        company = user.get('company', None)
        if company is not None:
            dict_to_template['company_name'] = company.get('name', 'название компании не указано')
        else:
            dict_to_template['company_name'] = 'пользователь не находится в компании'

        name_user = user.get('name', 'имя не указано')
        dict_to_template['name'] = name_user
        dict_to_template['email'] = user.get('email', 'почта не указана')
        dict_to_template['date_time'] = datetime.now().strftime("%d.%m.%Y %H:%M")

        user_id = user['id']
        finished_tasks_titles = []
        process_tasks_titles = []

        for task in all_tasks_list:
            task_user_id = task.get('userId', None)
            if task_user_id is not None and task_user_id == user_id:
                task_title = task.get('title', 'не указано')

                if len(task_title) > 48:
                    task_title = "".join([task_title[:48], "..."])
                completed_flag = task.get('completed', None)

                if completed_flag is not None:
                    finished_tasks_titles.append(
                        task_title) if completed_flag else process_tasks_titles.append(task_title)

        dict_to_template['finished_tasks'] = "\n".join(finished_tasks_titles)
        count_finished_tasks = len(finished_tasks_titles)
        dict_to_template['finished_tasks_count'] = count_finished_tasks

        dict_to_template['process_tasks'] = "\n".join(process_tasks_titles)
        count_process_tasks = len(process_tasks_titles)
        dict_to_template['process_tasks_count'] = count_process_tasks

        dict_to_template['general_tasks_count'] = count_finished_tasks + count_process_tasks

        report = template.safe_substitute(dict_to_template)
        create_and_write_txt_file_by_name(filename=name_user, data_to_write=report)
