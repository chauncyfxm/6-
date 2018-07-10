import requests
import lxml.etree

url = 'https://www.douban.com/search'
params = {
    'q':'成龙',
}
headers = {
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:57.0) Gecko/20100101 Firefox/57.0'
}
response = requests.get(url=url, params=params, headers=headers)
with open('ceshi.html','w') as f:
    f.write(response.text)

html = lxml.etree.HTML(response.text)
html_list = html.xpath('//div[@class="result-list"]/div[@class="result"]')
print(len(html_list))