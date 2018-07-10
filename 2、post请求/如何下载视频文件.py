import urllib.request as request
import urllib.parse as parse
import ssl


#目标url地址
# https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=4204913282,3820880852&fm=27&gp=0.jpg

def write_image_data(data,url):
    filename = url[-10:]
    with open(filename+'.mp4','wb') as f:
        f.write(data)
        print("已成功下载"+filename)

def main():
    context = ssl._create_unverified_context()

    url = 'https://n7-pl-agv.autohome.com.cn/video-28/966CE40A95BD238A/2018-07-02/D8DF3C666CF4768F-300.mp4?key=11A5CDE336695A528E91EAB21FF9C64A&time=1530590359'
    headers = {
         'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
    }

    req = request.Request(url,headers=headers)

    response = request.urlopen(req,context=context)

    print(response.status)

    imagedata = response.read()

    if response.status == 200:
        write_image_data(imagedata,url)

    
if __name__ == '__main__':
    main()