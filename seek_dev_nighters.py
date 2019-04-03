import requests
import datetime
import sys

url_template = 'http://devman.org/api/challenges/solution_attempts/'


def get_number_of_pages():
    try:
        response = requests.get(url_template)
        return int(response.json()['number_of_pages'])
    except (
            requests.exceptions.ConnectionError,
            requests.exceptions.ConnectTimeout,
    ):
        return


def load_attempts():
    pages = get_number_of_pages()
    if not pages:
        return
    for page in range(1, pages + 1):
        params = {
            'page': page,
        }
        try:
            response = requests.get(url_template, params)
            attempts = response.json()['records']
        except (
                requests.exceptions.ConnectionError,
                requests.exceptions.ConnectTimeout,
        ):
            return

        for attempt in attempts:
            yield attempt


def get_midnighters(attempts):
    for attempt in attempts:
        attempt_datetime = datetime.datetime.fromtimestamp(
            attempt['timestamp'])
        if attempt_datetime.time().hour == 0:
            yield {
                'username': attempt['username'],
                'time': attempt_datetime.isoformat(),
                'timezone': attempt['timezone'],
            }


def print_midnighter(midnighter):
    print(midnighter['username'])
    print(midnighter['time'])
    print(midnighter['timezone'])
    print()


if __name__ == '__main__':
    attempts = load_attempts()

    if not attempts:
        sys.exit("Connection error or server doesn't answer")

    print('Users who sent the tasks from 0 to 1 am:\n')

    for midnighter in get_midnighters(attempts):
        print_midnighter(midnighter)
