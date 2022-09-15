"""Модуль для получения данных пользователей и задач"""
import requests

BASE_URL = 'https://json.medrocket.ru/'
TODOS = 'todos'
USERS = 'users'


def get_users_list_from_api() -> list:
    """Возвращает список пользователей cо сторонней APi https://json.medrocket.ru/users"""
    response = requests.get("".join([BASE_URL, USERS]))
    return list(response.json())


def get_tasks_list_from_api() -> list:
    """Возвращает список задач cо сторонней APi https://json.medrocket.ru/todos"""

    response = requests.get("".join([BASE_URL, TODOS]))
    return list(response.json())

