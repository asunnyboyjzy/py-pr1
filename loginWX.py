@itchat.msg_register([itchat.content.TEXT], isGroupChat=True)  # ע��һ��Ⱥ��Ϣ�Ĵ���
def print_content(msg):
    if msg.User["NickName"] == qun:# ��������ں���Ӹ����or msg.User["NickName"]=='��ϣ���Զ��ظ�Ⱥ������
        if str(msg['Text'][0:5])=="https":#�����������Ϣ�ǲ������ӣ���ͨ��ǰ5��
            huifubdwk= GET_SHORTURL(str(msg['Text']))#���GET_SHORTURL����������˵���Ǹ����������Լ������
            print(msg.User['NickName'] + ":" + msg['Text'] )  # ��ӡ�ĸ�Ⱥ���㷢��ʲô��Ϣ
            print("%s+\n"%huifubdwk)  # ��ӡ�����˻ظ�����Ϣ
            itchat.send(u'@%s\u2005 %s' % (msg['ActualNickName'],huifubdwk), msg['FromUserName'])
        else:# ��������ֱ�Ӻ���
            print(msg['Text'])
    else:#������ӦȺֱ�Ӻ���
        pass