# Night Owls Detector

The app shows users from [DEVMAN.org](https://devman.org) who sent tasks for check after midnight (from 0 to 1 am)

# How to Install

Python 3 should be already installed. 
Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
$ pip install -r requirements.txt # alternatively try pip3
```

Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Quickstart

To use run the app from command line

```bash
$ python seek_dev_nighters.py
Users who sent the tasks from 0 to 1 am:

constantinovich
2019-04-02T00:43:17.652092+07:00
Asia/Novosibirsk

ekluev
2019-03-29T00:33:43.502227+03:00
Europe/Moscow

ekluev
2019-03-29T00:21:41.053172+03:00
Europe/Moscow
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)