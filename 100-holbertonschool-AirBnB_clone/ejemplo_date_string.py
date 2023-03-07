date_string = '2022-02-22T12:34:56.789012'

import datetime

date_string = datetime.datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%f')

print(date_string)
