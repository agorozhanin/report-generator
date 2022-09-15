from service.api_service import get_users_list_from_api
from service.files_service import create_tasks_directory_if_needed
from service.report_service import create_reports

if __name__ == '__main__':
    users = get_users_list_from_api()
    if len(users) != 0:
        create_tasks_directory_if_needed()
        create_reports(users_list=users)
