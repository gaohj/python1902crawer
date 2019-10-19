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

# print(driver.get_cookies())

for cookie in driver.get_cookies():
    print(cookie)


print("="*30)
driver.delete_all_cookies() #删除所有的cookie
print(driver.get_cookie('BD_UPN'))
#{'domain': 'www.baidu.com', 'expiry': 1572333546, 'httpOnly': False, 'name': 'BD_UPN', 'path': '/', 'secure': False, 'value': '12314753'}

driver.delete_cookie('BD_UPN') #删除制定的cookie
print(driver.get_cookie('BD_UPN')) #根据value 获取指定的cookie