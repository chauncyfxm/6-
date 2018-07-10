from selenium import webdriver

driver = webdriver.Chrome(executable_path='/home/chauncyfxm/桌面/geckodriver')
driver.get('http://www.baidu.com/')
driver.find_element_by_id('kw').send_keys('美女')

