from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://www.baidu.com')
import time
time.sleep(5)
driver.quit()