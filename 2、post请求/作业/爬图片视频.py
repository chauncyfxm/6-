# import sys
# import io
import urllib.request
import urllib.parse
import ssl
import urllib.error
import re

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码

# 创建文件夹
def mkdir(path):
    # 引入模块
    import os
 
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
 
        print(path+' 创建成功')
        return path
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path+' 目录已存在')
        return path
 
# 定义要创建的目录
# mkpath="d:\\qttc\\web\\"
# 调用函数
# mkdir(mkpath)


super_url = 'https://www.readnovel.com/rank/hotsales?'
status = True

def parameter():
    i = 1
    while True:
        # url
        dict = {
            'pageNum':i
        }
        dict1 = urllib.parse.urlencode(dict, encoding='utf-8')
        url = 'https://www.readnovel.com/rank/hotsales?'+ dict1
        
        
        # context
        context = ssl._create_unverified_context()

        # headers
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            'Cookie':'_csrfToken=1c5SF0w1Coghk4xA6vxWI2BhiODTiYFAkRUS4Kuk; newstatisticUUID=1530780906_1325563421',
            'Referer':'https://www.readnovel.com/rank/hotsales?pageNum=1',
        }
        
        response = run(url=url, headers=headers, context=context)
        html = response.read().decode()

        # 图片标题
        data1(html)

        # 每个章节
        data2(html)
        
        if not status:
            print('状态为'+str(status)+'停止请求')
            break
        i += 1

def run(url, headers, context=None, data=None):
    url1 = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(url1,context=context, data=data)
    return response
    


# 图片标题之类的
def data1(html):
    

    pattren = re.compile('<li.*?<span.*?([0-9]+)</span>.*?<img src="(.*?)">.*?<h4><a href.*?>(.*?)</a></h4>.*?<a .*?>(.*?)</a>.*?<a href=.*?>(.*?)</a>.*?<p .*?>(.*?)</p>.*?<span>(.*?)</span>',re.S)
    reslut = re.findall(pattren,html)


    if not bool(reslut):
        status = False
    
    else:
        for i in reslut:
            imgurl = 'http:'+i[1]

            headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
            }
            imgresponse = run(url=imgurl, headers=headers)
            imge = imgresponse.read()


            # 定义要创建的目录
            mkpath="D:\\6、爬虫初级\\2、post请求\\作业\\爬到的数据\\"+i[2]
            # 调用函数
            mkpath = mkdir(mkpath)
            path = mkpath + "\\" + i[2] + '.jpg'
            with open(path, 'wb') as f:
                f.write(imge)
            
            for a in i:
                path = mkpath + "\\" + '信息' + '.txt'
                with open(path, 'a+') as f:
                    f.write(a+'\n')




# 每个章节的名字
def data2(html):

    pattren = re.compile('<li data-rid=.*?<h4><a href="(.*?)".*?>(.*?)</a>',re.S)
    reslut = re.findall(pattren,html)
    

    if not bool(reslut):
        global status
        status = False
        print('爬到的数据是'+str(status))
    else:
        for i in reslut:
            list_url = urllib.parse.urljoin(super_url,i[0]+'#Catalog')

            headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
                'Cookie':'_csrfToken=1c5SF0w1Coghk4xA6vxWI2BhiODTiYFAkRUS4Kuk; newstatisticUUID=1530780906_1325563421; qdrs=0%7C3%7C0%7C0%7C1; qdgd=1'
            }
            
            response = run(url=list_url, headers=headers)
            html_list = response.read().decode('utf-8') #每个小说的列表页
            print('list页请请求状态' + str(response.status))

            if response.status == 200:
                print('list页面请求成功')
                content(html_list, i[1]) #把每个小说的所有章节传进去，把每个章节的内容保存起来

            # 定义要创建的目录
            # mkpath="D:\\6、爬虫初级\\2、post请求\\作业\\爬到的数据\\"+i[1]
            # 调用函数
            # mkpath = mkdir(mkpath)
            # path = mkpath + "\\" + i[2] + '.jpg'
            # with open(path, 'wb') as f:
            #     f.write(html_list)
            
            # for a in i:
            #     path = mkpath + "\\" + '信息' + '.txt'
            #     with open(path, 'a+') as f:
            #         f.write(a+'\n')

# 内容
def content(html_list_str, title):
    # 所有的章节和连接
    pattren = re.compile('<div.*?volume.*?<ul.*?</ul>',re.S)
    reslut = re.search(pattren, html_list_str)
    html_list_str_01 = reslut.group().encode()
    ceshi_file(html_list_str_01)
    # print(reslut.group())
    


    # 每个章节的内容


    pass
def ceshi_file(content):
    with open('ceshi.txt', 'wb') as f:
        f.write(content)
    f = open('ceshi.txt', 'r')
    f.read()
    print(f)
    f.close()


def main():
    parameter()

if __name__ == '__main__':
    main()
