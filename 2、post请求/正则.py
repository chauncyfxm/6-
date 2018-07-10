import re


string = '<div class="upload-fail-tip">请先设置语种，然后点击 [翻译] 按钮开始翻译</div>'
pattren = re.compile('<div(.*?)请',re.S)


reslut = re.match(pattren,string)
print(reslut.group(0))
print('第一次\n')


pattren = re.compile('<div(.*?)请',re.S)
reslut = re.findall(pattren, string)
print(reslut[0])
print('第二次\n')


pattren = re.compile('<div(.*?)请',re.S)
reslut = re.sub(pattren,'sddfsdfdsf', string)
print(reslut)
print('第三次\n')

pattren = re.compile('<div(.*?)请',re.S)
reslut = re.search(pattren,string)
print(reslut.group(0))
print('第四次\n')


pattren = re.compile('<',re.S)
reslut = re.split(pattren,string)
print(reslut.group(0))
print('第五次\n')
