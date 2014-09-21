import datetime
from datetime import date
import time

print 'time now : ' , time.time() # return number of seconds (1 enero 1970 to unix now)
print 'object tipo date : ' , date.fromtimestamp(123456789)
print 'conbinar funtions : ' , date.fromtimestamp(time.time())
currentDate = date.fromtimestamp(time.time())
print 'variable : ' , currentDate.strftime('%d/%m/%y')
