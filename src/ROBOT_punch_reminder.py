import base
from base import *
import datetime

WEEKDAYS = ['日','一','二','三','四','五','六',]
tz = datetime.timezone(datetime.timedelta(hours=8))

cst_now = datetime.datetime.now(tz=tz)
Y = cst_now.strftime('%Y')
m = cst_now.strftime('%m')
d = cst_now.strftime('%d')
w = WEEKDAYS[int(cst_now.strftime('%w'))]

mystr = '''\
# 药康码打卡
今天是**%s年%s月%s日星期%s**，请记得填写药康码。  
''' %(Y,m,d,w)

cst_today = datetime.datetime.strptime('%s-%s-%s'%(Y,m,d), '%Y-%m-%d').astimezone(tz)
cst_begin_term = datetime.datetime.strptime('2022-08-29', '%Y-%m-%d').astimezone(tz)
delta = cst_begin_term - cst_today
dd = delta.days
if dd > 0:
    mystr += '''\

-----------------
今天距离2022年8月29日第一节早九还有**%d**天。  
''' %(dd)

mystr += '''\
[点此查看校历(WEB)](https://jwc.cpu.edu.cn/7f/81/c867a163713/page.htm)  
[点此查看校历(PDF)](https://jwc.cpu.edu.cn/_upload/article/files/02/9f/78d41abf468980a72214bd411edf/9b54e4b6-1269-4d03-a4d9-6e14c8e74d50.pdf)
'''

if dd > 2:
    mystr += '''\

-----------------
今天距离2022年8月27日返校日还有**%d**天。  
''' %(dd-2)

if dd >= 7 and dd <= 11:
    mystr += '''\
请注意：2022年8月22日是返校申请可提交的最后一天，距此还剩**%d**天。  
''' %(dd-7)



with open(MYDIR + '/msg/msg.md','w',encoding='utf-8') as f:
    f.write(mystr)
