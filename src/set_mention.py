# python ./src/set_mention.py env_for_mentioned_list env_for_mentioned_mobile_list 1/0(mention all) 1/0(mention now)
import base
from base import *
def mystr(exp):
    if exp is None:
        return ''
    else:
        return str(exp)
mentioned_list = mystr(os.getenv(sys.argv[1]))
mentioned_mobile_list = mystr(os.getenv(sys.argv[2]))
with open(MYDIR + '/msg/mentioned.list','w',encoding='utf-8') as f:
    f.write(mentioned_list)
with open(MYDIR + '/msg/mentioned_mobile.list','w',encoding='utf-8') as f:
    f.write(mentioned_mobile_list)
if bool(int(sys.argv[3])):
    with open(MYDIR + '/msg/mentioned.list','a',encoding='utf-8') as f:
        f.write('@all\n')
if bool(int(sys.argv[4])):
    with open(MYDIR + '/msg/msg.txt','w',encoding='utf-8') as f:
        f.write('')
