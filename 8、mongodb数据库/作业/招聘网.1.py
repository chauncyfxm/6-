from selenium import webdriver
from lxml import etree
opt = webdriver.ChromeOptions()
opt.set_headless()
driver = webdriver.Chrome(executable_path='/home/chauncyfxm/git/code/6、爬虫/6-/驱动器/chromedriver')
driver.get('https://www.zhaopin.com/')

driver.find_element_by_class_name('zp-search-input').send_keys('爬虫')
driver.find_element_by_xpath('//a[@class="zp-search-btn zp-blue-button"]').click()
# driver.find_element_by_xpath('//div[@id="sou_showTypes"]//div[@class="showType"]/span[@class="showType_simple-checked"]').click()
# driver.find_element_by_xpath('//div[@id="pagination_content"]//button[@class="btn btn-pager"]').click()

# print(driver.page_source)
xpath_html = etree.HTML(driver.page_source)
list = xpath_html.xpath('div[@id="listContent"]//div[@class="listItemBox clearfix"]')

print(len(list))


# driver.close()