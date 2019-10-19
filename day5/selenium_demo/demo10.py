from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
#导入行为链
from selenium.webdriver.common.by import By
#chromedriver的绝对路径
driver_path = r'C:\chromedriver\chromedriver.exe'

#初始化一个driver对象
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.baidu.com")


submitBtn = driver.find_element(By.ID,'su')
print(type(submitBtn))#<class 'selenium.webdriver.remote.webelement.WebElement'>
print(submitBtn.get_attribute('value'))#百度一下

driver.save_screenshot('baidu.png')