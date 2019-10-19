from selenium import webdriver
import time
from selenium.webdriver.common.by import By
#chromedriver的绝对路径
driver_path = r'C:\chromedriver\chromedriver.exe'

#初始化一个driver对象
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("http://www.baidu.com")
# inputTag = driver.find_element_by_id('kw')
# inputTag = driver.find_element_by_name('wd')
# inputTag = driver.find_element_by_css_selector(".quickdelete-wrap > input")
# inputTag = driver.find_element_by_xpath("//*[@id='kw']")
# inputTag = driver.find_element(By.ID,'kw')
# inputTag = driver.find_element(By.NAME,'wd')
# inputTag = driver.find_element(By.CSS_SELECTOR,'.quickdelete-wrap > input')
#inputTag = driver.find_elements(By.CSS_SELECTOR,'.quickdelete-wrap > input')[0]
inputTag = driver.find_elements(By.XPATH,"//input[@id='kw']")[0]
# print(inputTag)
inputTag.send_keys('岛国是哪里?')


submitTag = driver.find_element(By.ID,'su')
submitTag.click()
time.sleep(5)
inputTag.clear() #清空输入框内容
driver.quit()
