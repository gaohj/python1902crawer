from selenium import webdriver
import time
from selenium.webdriver.common.by import By
#chromedriver的绝对路径
driver_path = r'C:\chromedriver\chromedriver.exe'

#初始化一个driver对象
driver = webdriver.Chrome(executable_path=driver_path)
driver.get("https://v3.bootcss.com/examples/signin/")

remembers = driver.find_element(By.XPATH,'//input[@value="remember-me"]')
remembers.click()