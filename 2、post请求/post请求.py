import urllib.request
import urllib.parse
import ssl

# https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false




def parameter():
    # url
    dict = {
        'needAddtionalResult':'false'
    }
    dict1 = urllib.parse.urlencode(dict, encoding='utf-8')
    url = 'https://www.lagou.com/jobs/positionAjax.json?'+ dict1
    
    # from表单
    from_data = {
        'first':'true',
        'pn':'1',
        'kd':'python'
    }
    data = urllib.parse.urlencode(dict, encoding='utf-8').encode('utf-8')
    
    # context
    context = ssl._create_unverified_context()

    # headers
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'Cookie':'JSESSIONID=ABAAABAACEBACDG5BB68254B6E4613B2104B824C5CAB126; _ga=GA1.2.870885106.1530757565; _gid=GA1.2.149299373.1530757565; _gat=1; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1530757567; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_search; user_trace_token=20180705102614-60387d11-df59-4eb8-a0d6-f01e0d90191f; LGSID=20180705102615-caee337c-7ffa-11e8-98e3-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_python%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; LGRID=20180705102615-caee34f2-7ffa-11e8-98e3-5254005c3644; LGUID=20180705102615-caee3564-7ffa-11e8-98e3-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1530757575; SEARCH_ID=3bbe1c00cfc04ac5a5f83229e4808d19',
        'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    }
    run(url=url, headers=headers, context=context, data=data)

def run(url, headers, context, data):
    url1 = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(url1,context=context, data=data)
    print(response.read().decode())



def main():
    parameter()

if __name__ == '__main__':
    main()