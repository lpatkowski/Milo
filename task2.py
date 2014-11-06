import time
from datetime import datetime
import sys

read = open("input.txt", "r").read()

return_value = 0
values = list(read.split('/'))

count = 0
for v in values:
    if len(v) in (1,3):
        values[count] = '0' + v
    if int(v) == 0:
        values[count] = '2000' 
    count += 1

matrix = [
    [values[0],values[1],values[2]],
    [values[0],values[2],values[1]],
    [values[1],values[0],values[2]],
    [values[1],values[2],values[0]],
    [values[2],values[1],values[0]],
    [values[2],values[0],values[1]],
]

datetimes = []

for v in matrix:
    try:
        new_datetime = datetime(int(v[0]),int(v[1]),int(v[2]),0,0)
        datetimes.append({'date':new_datetime.date(),'seconds':time.mktime(new_datetime.timetuple()),})
    except ValueError, e:
        continue

if datetimes:
    datetimes = sorted(datetimes, key=lambda x: x['seconds'])
    for datetime in datetimes:
        if datetime['date'].year >= 2000 and datetime['date'].year <= 2999:
            return_value = datetime['date']
            break
        elif datetime['date'].year < 100:
            datetime['date'] = datetime['date'].replace(year=datetime['date'].year+2000)
            return_value = datetime['date']
            break
    
print >> sys.stdout,  return_value




            
