import requests
from bs4 import BeautifulSoup
import urllib


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






url = 'https://www.jianshu.com/c/7b2be866f564'

params = {
    'utm_medium':'index-collections',
    'index-collections':'desktop',
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

response = requests.get(url=url, params=params, headers= headers)

with open("ceshi.html","w") as f:
    f.write(response.text)

# 实例化soup对象
soup = BeautifulSoup(response.text,'lxml')
div_list = soup.select('#list-container')
# print(div_list)

title_list = div_list[0].select('a.title')

li_list = div_list[0].select('li.have-img')
print(len(li_list))


for i in li_list:
    title = i.select('a.title')[0].string
    t_url = i.select('a.title')[0]['href']
    img_url = i.select('a.wrap-img img')[0]['src']

    comments_count = i.select('a[target="_blank"]')[0].string



    print(img_url)

    t_url = urllib.parse.urljoin(url,t_url)
    img_url = urllib.parse.urljoin(url,img_url)

    print(t_url)

    # 开始请求
    response = requests.get(url=t_url, headers= headers)
    print(response.status_code)
    # 匹配
    soup = BeautifulSoup(response.text,'lxml')

    zuozhe = soup.select('div.author div.info span.name a')[0].string
    datetime = soup.select('div.author div.info div.meta span.publish-time')[0].string
    # views_count = soup.select('div.author div.info div.meta span.views-count')[0].string
    # views_count = soup.select('div.author div.info')
    # print(views_count)
    # comments_count = soup.select('div.author div.info div.meta span.comments-count')[0].string
    content1 = soup.select('div.show-content p')
    for a in content1:
        content = ''
        content = content + str(a.string)
    print(content)

    # 定义要创建的目录
    mkpath="/home/chauncyfxm/6、爬虫初级/5、beautifulsoup模/" + title
    # 调用函数
    mkpath = mkdir(mkpath)
    with open(mkpath+'/'+title+'.txt','a+') as f:
        f.write('标题是：'+zuozhe+'/n')
        f.write('评论是：'+str(comments_count)+'/n')
        f.write('时间是：'+datetime+'/n')
        f.write('内容是：'+content+'/n')

    img_response = requests.get(url=img_url, headers= headers)
    print(img_response.status_code)
    with open(mkpath+'/'+title+'.jpg','wb') as f:
        f.write(img_response.content)
        
    
    


        












