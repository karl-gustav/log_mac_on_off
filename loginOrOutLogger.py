#! /usr/bin/python

import time
import sys
import os


TAG = sys.argv[1]
LOG_PATH = os.path.expanduser("~/login_logout.log")
now = time.strftime("%Y-%m-%dT%H:%M:%S")

data = ""
if os.path.isfile(LOG_PATH):
    with file(LOG_PATH, 'r') as original: data = original.read()
with file(LOG_PATH, 'w+') as modified: modified.write("%s %s \n" % (TAG, now) + data)
