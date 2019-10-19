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

inputTag = driver.find_elements(By.XPATH,"//input[@id='kw']")[0]
submitTag = driver.find_element(By.ID,'su')

actions = ActionChains(driver)
actions.move_to_element(inputTag) #移动到 输入框
actions.send_keys_to_element(inputTag,'python') #往输入框写内容
actions.move_to_element(submitTag) #移动到点击按钮
actions.click(submitTag) #单击
actions.perform() #执行
