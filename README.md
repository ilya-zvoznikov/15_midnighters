# Night Owls Detector

The app shows users from [DEVMAN.org](https://devman.org) who sent tasks for check after midnight (from 0 to 6 am)

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
Users who sent the tasks from 0 to 6 am:

constantinovich
2019-04-03 05:37:06.222063+07:00
2019-04-02 00:43:17.652092+07:00
2019-03-26 00:31:10.020308+07:00
2019-03-19 00:14:57.412569+07:00
2019-03-13 00:03:29.959189+07:00
2019-03-07 00:08:49.039497+07:00

ekluev
2019-03-29 00:33:43.502227+03:00
2019-03-29 00:21:41.053172+03:00
2019-03-29 00:17:24.343396+03:00
2019-03-29 00:11:10.910401+03:00

1d964ba0d0604b37
2019-03-20 00:00:14.665558+03:00

PeterChe
2019-04-04 00:31:38.820442+02:00

seregan777
2019-03-30 05:59:10.236078+03:00

idmedvedevivan
2019-03-05 00:49:31.430813+03:00

andreishkilev1993
2019-04-02 03:27:04.253617+03:00
2019-04-02 01:39:38.527911+03:00
2019-03-30 02:02:28.221595+03:00
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)