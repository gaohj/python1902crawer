from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class QiangPiao(object):
    def __init__(self):
        self.options = Options()
        self.options.add_argument('--disable-gpu')
        self.login_url = 'https://kyfw.12306.cn/otn/login/init'
        self.my12306_url = 'https://kyfw.12306.cn/otn/view/index.html'
        self.search_url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'
        self.passenger_url = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'
        self.driver = webdriver.Chrome(chrome_options=self.options)

    def wait_input(self):
        self.from_station = input("请输入出发地:")
        self.to_station = input("请输入目的地:")
        self.depart_time = input("请输入出发时间:")
        self.passengers = input("乘客姓名:(多个乘客请用英文,隔开)").split(',')
        self.trains = input("车次:(多个车次用英文,隔开)").split(',')

    def _login(self):
        self.driver.get(self.login_url)
        WebDriverWait(self.driver,1000).until(
            EC.url_to_be(self.my12306_url)
        )
        print('登录成功')

    def _order_ticket(self):
        self.driver.get(self.search_url)
        print(self.from_station)
        #等待出发地是否输入正确  显性
        WebDriverWait(self.driver,10).until(
            EC.text_to_be_present_in_element_value((By.ID,"fromStationText"),self.from_station)
        )


        #目的地
        WebDriverWait(self.driver,10).until(
            EC.text_to_be_present_in_element_value((By.ID, "toStationText"), self.to_station)
        )

        #出发日期
        WebDriverWait(self.driver,10).until(
            EC.text_to_be_present_in_element_value((By.ID, "train_date"), self.depart_time)
        )

        #查看 按钮是否可用
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "query_ticket"))
        )

        #如果可用 找到它 并点击它
        searchBtn = self.driver.find_element(By.ID,"query_ticket")
        searchBtn.click()


    def run(self):
        self.wait_input()
        self._login()
        self._order_ticket()


if __name__ == "__main__":
    spider = QiangPiao()
    spider.run()