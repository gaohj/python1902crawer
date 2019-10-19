from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#chromedriver的绝对路径
driver_path = r'C:\chromedriver\chromedriver.exe'

#初始化一个driver对象
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.douban.com")
# driver.implicitly_wait(10)
# driver.get("https://www.douban.com")
#
# rem_btn = driver.find_element(By.ID,'account-form-remember')
# print(rem_btn)

element= WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.ID,'username'))
)

print(element)
