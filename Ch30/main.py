import datetime

timeStop = datetime.datetime(2021,9,8,11,1,0)
while datetime.datetime.now() < timeStop:
    print('sleeping')
print('wake up')