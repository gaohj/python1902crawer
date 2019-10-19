from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
#导入行为链
from selenium.webdriver.common.by import By
#chromedriver的绝对路径
driver_path = r'C:\chromedriver\chromedriver.exe'
options = webdriver.ChromeOptions()  #创建代理对象

options.add_argument("--proxy-server=http://218.14.109.42:54179") #设置代理地址
options.add_argument("--headless") #无界面形态
options.add_argument("--disable-gpu") #禁gpu
#初始化一个driver对象
driver = webdriver.Chrome(executable_path=driver_path,chrome_options=options)
driver.get("http://httpbin.org/ip")
print(driver.page_source)
time.sleep(15)

driver.quit()