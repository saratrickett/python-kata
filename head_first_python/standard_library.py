import sys
print(sys.version)
print(sys.platform)

# name of folder you are operating in
import os
print(os.getcwd())
print (os.environ)
# system's environment variables

import datetime
print(datetime.date.today())
print(datetime.date.today().day)
print(datetime.date.today().month)
print(datetime.date.today().year)
print(datetime.date.isoformat(datetime.date.today()))

import time
print(time.strftime('%H:%M:%S'))
print(time.strftime ('%A %p'))
