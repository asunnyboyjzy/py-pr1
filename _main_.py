import requests
    firsturl=input('�������ĵ����ӣ�')
    # �����õ����������ӣ�һ���ǲ�ѯ�ĵ�ID�ģ���һ�������ص�
    url1 = "http://139.224.236.108/post.php"
    url3 = "http://139.224.236.108/downdoc.php"
    # ��������ĵ����ӽ���ת��
    downloadurl = firsturl.replace("/", "%2F").replace(":", "%3A")

    # head1��ѯ�ĵ�ID������ͷ
    # data1�ǲ�ѯ���������ݣ����н�docinfo��ֵת��Ϊ����
    # ��ѯ�õ��������ȡid����һ�β�����
    def query():
        head1 = {"POST": "/post.php HTTP/1.1",
             "Host": "139.224.236.108",
             "Content-Length": "145",
             "Accept": "*/*",
             "Origin": "http://139.224.236.108",
             "X-Requested-With": "XMLHttpRequest",
             "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
             "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
             "Referer": "http://139.224.236.108/1.html",
             "Accept-Encoding": "gzip, deflate",
             "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
             "Cookie": "usrname=901961495; usrpwd=559448"
             }
        data1 = 'usrname=901961495&usrpass=559448&docinfo=downloadurl&taskid=up_down_doc1'
        data1 = data1.replace('downloadurl', downloadurl)
        respons = requests.post(url1, data=data1, headers=head1).json()
        id = respons['url']
        id = id[37:]
        return id

    id = query()

    # head3�����ĵ�������ͷ
    # data3���������ص��������ݣ�����vid�ǲ�ѯ���ݷ��ص��ĵ�idֵ
    # ��ȡ��������
    def down():
        Referer = "http://139.224.236.108/nocode.php?id={docid}"
        head3 = {"POST": "/downdoc.php HTTP/1.1",
             "Host": "139.224.236.108",
             "Content-Length": "54",
             "Accept": "*/*",
             "Origin": "http://139.224.236.108",
             "X-Requested-With": "XMLHttpRequest",
             "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
             "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
             "Referer": Referer.format(docid=id),
             "Accept-Encoding": "gzip, deflate",
             "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
             "Cookie": "usrname=901961495; usrpwd=559448"
             }
        data3 = 'vid={docid}&taskid=directDown'
        data3 = data3.format(docid=id)
        response = requests.post(url3, data=data3, headers=head3).json()
        downurl = response["dlink"].replace("\\", '')
        print(downurl)#������URL�����Զ������ļ�Ŷ
        return downurl

query()
down()