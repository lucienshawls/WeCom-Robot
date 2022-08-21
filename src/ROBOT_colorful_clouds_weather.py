import base
from base import *
token = os.getenv('COLORFUL_CLOUDS_WEATHER_API_TOKEN')

import time
import requests

location = ('118.915949','31.901664')
import datetime

WEEKDAYS = ['日','一','二','三','四','五','六',]
tz = datetime.timezone(datetime.timedelta(hours=8))

cst_now = datetime.datetime.now(tz=tz)
Y = cst_now.strftime('%Y')
m = cst_now.strftime('%m')
d = cst_now.strftime('%d')
w = WEEKDAYS[int(cst_now.strftime('%w'))]

# URL = "http://api.caiyunapp.com"
# MAX_RETRY = 3
# data = {}

# retry_times = 0
# while retry_times <= MAX_RETRY:
#   try:
#     data = requests.get(URL).json()
#     break
#   except Exception:
#     print("failed")
#     retry_times += 1
#     time.sleep(retry_times*retry_times)
#     continue

# print(data)
def daily():
    params = {'dailysteps': '1','lang': 'zh_CN'}

    response = requests.get('https://api.caiyunapp.com/v2.6/%s/%s,%s/daily' %(token,location[0],location[1]), params=params)
    print(response.text)

def hourly():
    pass
def write_data():
    mystr = '''\
# 天气简报
**%s年%s月%s日星期%s**，请查收今日天气。  
''' %(Y,m,d,w)
    if True: # 有预警
        mystr += '''\
## 气象预警
（预警信息）
'''
    mystr += '''\
## 今日天气

'''
    with open(MYDIR + '/msg/msg.md','w',encoding='utf-8') as f:
        f.write(mystr)
