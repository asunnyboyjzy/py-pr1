import requests
    firsturl=input('请输入文档链接：')
    # 以下用到了两个链接，一个是查询文档ID的，另一个是下载的
    url1 = "http://139.224.236.108/post.php"
    url3 = "http://139.224.236.108/downdoc.php"
    # 将传入的文档链接进行转化
    downloadurl = firsturl.replace("/", "%2F").replace(":", "%3A")

    # head1查询文档ID的数据头
    # data1是查询的数据内容，其中将docinfo的值转化为链接
    # 查询得到结果，截取id的那一段并返回
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

    # head3下载文档的数据头
    # data3是请求下载的数据内容，其中vid是查询内容返回的文档id值
    # 获取下载链接
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
        print(downurl)#点击这个URL，会自动下载文件哦
        return downurl

query()
down()