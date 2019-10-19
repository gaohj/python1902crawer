from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

chrome_options = Options()
# chrome_options.add_argument('--proxy-server=')
chrome_options.add_argument('--headless')
#初始化一个driver对象
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.baidu.com")

print(driver.page_source)