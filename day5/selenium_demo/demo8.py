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


#在这个窗口中打开一个新的页面
driver.execute_script("window.open('https://www.zhihu.com/')")

print(driver.window_handles)

driver.switch_to_window(driver.window_handles[0])

time.sleep(10)

driver.quit()