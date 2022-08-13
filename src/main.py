import os
from mybase_lucien import mylocale
MYDIR = os.path.dirname(mylocale.get_dir(myfile=__file__))

def read_data(mode):
    json_data = {
        'msgtype': mode,
        mode: {}
    }
    if mode == 'text':
        with open(MYDIR + "/msg/msg.txt", "r",encoding='utf-8') as f:
            json_data[mode]['content'] = f.read()
        with open(MYDIR + "/msg/mentioned.list", "r",encoding='utf-8') as f:
            json_data[mode]['mentioned_list'] = f.read().strip().split('\n')
        with open(MYDIR + "/msg/mentioned_mobile.list", "r",encoding='utf-8') as f:
            json_data[mode]['mentioned_mobile_list'] = f.read().strip().split('\n')
    elif mode == 'markdown':
        with open(MYDIR + "/msg/msg.md", "r",encoding='utf-8') as f:
            json_data[mode]['content'] = f.read()
    elif mode == 'image':
        pass
    elif mode == 'news':
        pass
    else:
        pass
    return json_data

def send_msg(key,json_data):
    url_base = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send'
    params = {'key': key}
    import requests
    response = requests.post(url_base, params=params, json=json_data)
    return response
def main():
    mode = os.getenv('BOT_MODE')
    key = os.getenv('BOT_KEY')
    resp = send_msg(key,read_data(mode))

if __name__=='__main__':
    main()
