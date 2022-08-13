import main
import datetime
WEEKDAYS = ['日','一','二','三','四','五','六',]
cst_now = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8)))
Y = cst_now.strftime('%Y')
m = cst_now.strftime('%m')
d = cst_now.strftime('%d')
w = WEEKDAYS[int(cst_now.strftime('%w'))]
mystr = '''\
# 药康码打卡
今天是**%s年%s月%s日星期%s**，请记得填写药康码。
''' %(Y,m,d,w)
cst_today = datetime.datetime.strptime('%s-%s-%s'%(Y,m,d), '%Y-%m-%d').astimezone(datetime.timezone(datetime.timedelta(hours=8)))
cst_begin_term = datetime.datetime.strptime('2022-08-29', '%Y-%m-%d').astimezone(datetime.timezone(datetime.timedelta(hours=8)))
delta = cst_begin_term - cst_today
dd = delta.days
if dd > 0:
    mystr += '''\

-----
今天距离2022年8月29日第一节早八还有%d天。
'''%(dd)
with open(main.MYDIR + '/msg/msg.md','w',encoding='utf-8') as f:
    f.write(mystr)
