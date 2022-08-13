import main
mystr = '''\
# 药康码打卡
今天是**%d月%d日**，请记得填写药康码。

-----
如果你是在微信而不是企业微信看到的这条消息，你可以点击下面的链接直达药康码：  
[立即填写药康码](https://dform.cpu.edu.cn/tb.html)
''' %(8,13)
with open(main.MYDIR + '/msg/msg.md','w',encoding='utf-8') as f:
    f.write(mystr)
