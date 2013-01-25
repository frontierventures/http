#!/usr/bin/env python
import os
import time
from datetime import datetime


class color:
    HEADER = '\033[1;45m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'

    def disable(self):
        self.HEADER = ''
        self.GREEN = ''
        self.YELLOW = ''
        self.RED = ''
        self.ENDC = ''
#LOCAL
app = os.path.dirname(os.path.realpath(__file__)) + '/'
python = '/usr/local/bin/python2.7'


def timestamp():
    return time.time()


def convertTimestamp(timestamp):
    utc = datetime.utcfromtimestamp(timestamp)
    format = "%a %e %b %Y %r %Z"
    timestamp = utc.strftime(format)
    return timestamp
