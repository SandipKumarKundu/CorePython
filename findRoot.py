from datetime import datetime
import os
import sys
print (sys.platform)
print(os.getenv("localhost_debugging"))

date = datetime.now()
print(type(date) == datetime)
