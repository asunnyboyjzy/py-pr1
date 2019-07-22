@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)  # 注册一个群消息的处理
def print_content(msg):
    if msg.User["NickName"] == qun:# 这里可以在后面加更多的or msg.User["NickName"]=='你希望自动回复群的名字
        if str(msg['Text'][0:5])=="https":#检测所发的消息是不是链接，是通过前5个
            huifubdwk= GET_SHORTURL(str(msg['Text']))#这个GET_SHORTURL是我上面所说的那个函数，我自己定义的
            print(msg.User['NickName'] + ":" + msg['Text'] )  # 打印哪个群给你发了什么消息
            print("%s+\n"%huifubdwk)  # 打印机器人回复的消息
            itchat.send(u'@%s\u2005 %s' % (msg['ActualNickName'],huifubdwk), msg['FromUserName'])
        else:# 不是链接直接忽略
            print(msg['Text'])
    else:#不是相应群直接忽略
        pass