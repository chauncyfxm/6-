import urllib.request
import ssl
import urllib.parse
import io


# ssl证书
context = ssl._create_unverified_context()
# 请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
# 搜索内容
wd = input('请输入要搜索的内容：')


for i in range(0,3):
    pn = i*10
    dict = {
        'wd':wd,
        'pn':pn,
        'oq':wd
    }
    q = urllib.parse.urlencode(query=dict,encoding='utf-8')

    url = 'https://www.baidu.com/s?'+q+'&ie=utf-8&rsv_idx=1&rsv_pq=938e0740000364e3&rsv_t=0448of88dv20iMDKkhrUOvsI0saZIjB4Ux%2FQ33G%2BYeVYQbDpNpEb6%2FgjN9Y'
    url1 = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(url1, context=context)
    content = response.read().decode('gbk')

    f1 = 'a'+str(i)+'.html'
    with open(f1,'w') as f:
        f.write(content)
    