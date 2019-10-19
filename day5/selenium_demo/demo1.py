from selenium import webdriver

#chromedriver的绝对路径
driver_path = r'C:\chromedriver\chromedriver.exe'

#初始化一个driver对象
driver = webdriver.Chrome(executable_path=driver_path)

#请求网页
driver.get("http://www.baidu.com")

#获取百度源代码

print(driver.page_source)

