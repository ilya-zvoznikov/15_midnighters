import requests
import datetime
import sys
import pytz
from collections import defaultdict

URL = 'http://devman.org/api/challenges/solution_attempts/'
START_HOUR = 0
END_HOUR = 6


def load_attempts():
    page = 1
    while True:
        params = {
            'page': page,
        }
        try:
            response = requests.get(URL, params)
            attempts = response.json()
        except (
                requests.exceptions.ConnectionError,
                requests.exceptions.ConnectTimeout,
        ):
            return

        yield from attempts['records']

        if page < attempts['number_of_pages']:
            page += 1
        else:
            break


def get_midnighters(attempts, start_hour, end_hour):
    midnighters = defaultdict(list)
    for attempt in attempts:
        tz = pytz.timezone(attempt['timezone'])
        attempt_datetime = datetime.datetime.fromtimestamp(
            attempt['timestamp'],
            tz=tz,
        )
        if attempt_datetime.hour in range(start_hour, end_hour):
            midnighters[attempt['username']].append(attempt_datetime)
    return midnighters


def print_midnighters(midnighters):
    for midhighter, attempts_time_list in midnighters.items():
        print(midhighter)
        for attempt_time in attempts_time_list:
            print(attempt_time)
        print()


if __name__ == '__main__':
    attempts = load_attempts()

    if attempts is None:
        sys.exit("Connection error or server doesn't answer")

    print('Users who sent the tasks from {} to {} am:\n'.format(
        START_HOUR,
        END_HOUR
    ))

    midnighters = get_midnighters(attempts, START_HOUR, END_HOUR)
    print_midnighters(midnighters)
