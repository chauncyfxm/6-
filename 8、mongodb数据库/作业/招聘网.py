from selenium import webdriver
from lxml import etree
import csv
from bs4 import BeautifulSoup
opt = webdriver.ChromeOptions()
opt.set_headless()
driver = webdriver.Chrome(executable_path='/home/chauncyfxm/git/code/6、爬虫/6-/驱动器/chromedriver')
driver.get('https://www.zhaopin.com/')

driver.find_element_by_class_name('return-to-old').click()
driver.find_element_by_id('KeyWord_kw2').send_keys('in')
driver.find_element_by_class_name('doSearch').click()

s_html = driver.page_source
while True:
    xpath_html = etree.HTML(driver.page_source)
    xpath_list = xpath_html.xpath('//*[@id="newlist_list_content_table"]/table')
    list = []
    for i in xpath_list:
        name1 = i.xpath('./tbody/tr[1]/td[1]/div/a[1]')
        if bool(name1):
            name = name1[0].xpath('string(.)').strip()
            print(name)

        baifenbai = i.xpath('./tbody/tr[1]/td[2]/span/text()')
        if not bool(baifenbai):
            baifenbai = ['0%']
        baifenbai = baifenbai[0]
        
        gongsiname = i.xpath('./tbody/tr[1]/td[3]/a[1]/text()')
        if bool(gongsiname):
            gongsiname = gongsiname[0]
        
        wages = i.xpath('./tbody/tr[1]/td[4]/text()')
        if bool(wages):
            wages = wages[0]
        
        plac = i.xpath("./tbody/tr[1]/td[5]/text()")
        if bool(plac):
            plac = plac[0]

        datetime = i.xpath("./tbody/tr[1]/td[6]/span/text()")
        if bool(datetime):
            datetime = datetime[0]

        if bool(name1):
            dict = {
                'name':name,
                'baifenbai':baifenbai,
                'gongsiname':gongsiname,
                'wages':wages,
                'plac':plac,
                'datetime':datetime
            }
            list.append(dict)


    csvfile = open('./招聘信息.csv','w')
    writehandler = csv.DictWriter(csvfile, fieldnames=['name','baifenbai','gongsiname','wages','plac','datetime'])
    writehandler.writeheader()
    writehandler.writerows(list)

    # 判断是否到最后一页
    s_html = driver.page_source

    # 下一页
    try:
        page = driver.find_element_by_id('goto')
        page.send_keys()
        driver.find_element_by_class_name('next-page').click()
    except:
        break

    if s_html == driver.page_source:
        break

driver.close()