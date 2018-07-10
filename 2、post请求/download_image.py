import urllib.request as request
import ssl

#将获取的图片写入本地文件
def write_image_data(image_data,url):
    filename = url[-20:]
    #wb表示写入二进制文件
    with open(filename,'wb') as f:
        print('写入图片')
        f.write(image_data)

#将获取的视频写入本地文件
def write_video_data(video_data,url):
    filename = url[-10:]
    with open(filename+'.mp4','wb') as f:
        f.write(video_data)
        print('写入视频')
        
def main():
    # 图片的地址
    imageurl = 'https://qnwww2.autoimg.cn/youchuang/g27/M05/AC/4C/autohomecar__wKgHHls8sYOAZc13AATZCypW09E301.JPG?imageView2/1/w/590/h/344'
    #视频地址
    videourl = 'https://n7-pl-agv.autohome.com.cn/video-28/966CE40A95BD238A/2018-07-02/D8DF3C666CF4768F-300.mp4?key=11A5CDE336695A528E91EAB21FF9C64A&time=1530590359'
    #构造亲求对象
    headers = {
         'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:60.0) Gecko/20100101 Firefox/60.0',
    }
    req = request.Request(videourl,headers=headers)
    #获取响应结果
    response = request.urlopen(req,context=ssl._create_unverified_context())
    #打印请求状态码
    print(response.status)
    #读取数据，此时为字节流类型
    print(response.read())
    #字节流（二进制）
    # image_data = response.read()
    # write_image_data(image_data,imageurl)
    #视频数据
    video_data = response.read()
    #调用方法将视频写入本地文件
    write_video_data(video_data,videourl)
    
if __name__ == '__main__':
    main()
