import time
import turtle 
lala=turtle.Pen()
lala.forward(100)
now = time.gmtime()
print(now)

day = now.tm_mday
month = now.tm_mon
print(month)
print(day)

month = 3
day = 15

if (month == 3):
    if (day == 15):
        print('生日快乐')
        lala.write('生日快乐')
if (month == 7):
    if (day == 27):
        print('妈妈，生日快乐')
    if (day == 30):
        print('爸爸，生日快乐')
if (month == 6):
    if (day == 21):
        print('父亲节快乐')
if (month == 5):
    if (day == 10):
        print('母亲节快乐')
if (month == 12):
    if (day == 7):
        print('大雪')
turtle.done()
