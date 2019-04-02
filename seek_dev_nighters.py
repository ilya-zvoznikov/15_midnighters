import requests
import pytz

url_template = 'http://devman.org/api/challenges/solution_attempts/'


def get_number_of_pages():
    response = requests.get(url_template)
    return int(response.json()['number_of_pages'])


def load_attempts():
    pages = get_number_of_pages()

    for page in range(1, pages + 1):
        params = {
            'page': page,
        }
        response = requests.get(url_template, params)
        attempts = response.json()['records']
        for attempt in attempts:
            yield {
                'username': attempt['username'],
                'timestamp': attempt['timestamp'],
                'timezone': attempt['timezone'],
            }


def get_midnighters():
    pass


if __name__ == '__main__':
    for i in load_attempts():
        print(i)
