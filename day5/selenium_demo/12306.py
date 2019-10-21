#encoding: utf-8
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


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
        self.driver.get(self.login_url)  #跳转到登录页面
        WebDriverWait(self.driver,1000).until(
            EC.url_to_be(self.my12306_url)  #再切换到my12306_url 之前等待
        )
        print('登录成功')

    def _order_ticket(self):
        self.driver.get(self.search_url)

        print(self.from_station)
        inputTag = self.driver.find_element(By.ID,'fromStationText')
        print(inputTag)
        inputTag.send_keys(self.from_station)

        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, 'fromStationText'), self.from_station)
        )
        # 等待目的地是否输入正确

        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, 'toStationText'), self.to_station)
        )
        # 等待出发日期是否输入正确
        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, 'train_date'), self.depart_time)
        )

        # 查询按钮是否可用
        WebDriverWait(self.driver, 1000).until(
            EC.element_to_be_clickable((By.ID, 'query_ticket'))
        )
        # 如果能被点击就找到这个查询按钮
        searchBtn = self.driver.find_element_by_id('query_ticket')
        searchBtn.click()

        #点击了查询按钮以后 等待车次的信息是否展示出来了
        WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, './/tbody[@id="queryLeftTable"]/tr')) #满足这个条件的元素是否被加载出来了
        )

        #找到所有储存车次信息的tr
        #每个车次信息 两个tr 带有datatran属性的tr 没有内容 不是我们想要的 所以排除
        tr_lists = self.driver.find_elements_by_xpath(".//tbody[@id='queryLeftTable']/tr[not(@datatran)]")


        #遍历所有符合要求的tr
        for tr in tr_lists:
            train_number = tr.find_element_by_class_name("number").text
            print(train_number)
            if train_number in self.trains:
                #二等座
                left_tickets = tr.find_element_by_xpath(".//td[4]").text
                print(left_tickets)
                if left_tickets == "有" or left_tickets.isdigit:
                    order_btn = tr.find_element_by_class_name("btn72")
                    order_btn.click()

                    #等待你确实到了 选择买票人员页面了
                    WebDriverWait(self.driver, 1000).until(
                        EC.url_to_be(self.passenger_url)
                    )

                    #等待所有的乘客加载完毕
                    WebDriverWait(self.driver, 1000).until(
                        EC.presence_of_element_located((By.XPATH, './/ul[@id="normal_passenger_id"]/li'))
                        # 满足这个条件的元素是否被加载出来了
                    )

                    #获取所有的乘客信息
                    passengers = self.driver.find_elements_by_xpath(".//ul[@id='normal_passenger_id']/li/label")

                    for passenger in  passengers:
                        name = passenger.text
                        if name in self.passengers:
                            passenger.click()

                #获取提交订单的按钮

                submitBtn = self.driver.find_element_by_id('submitOrder_id')
                submitBtn.click()

                #等待确认对话框出现
                WebDriverWait(self.driver, 1000).until(
                    EC.presence_of_element_located((By.CLASS_NAME,'dhtmlx_wins_body_inner'))
                )


                #确认按钮是否也出现了
                WebDriverWait(self.driver, 1000).until(
                    EC.presence_of_element_located((By.ID, 'qr_submit_id'))
                )

                confirmBtn = self.driver.find_element_by_id('qr_submit_id')
                confirmBtn.click()

                while confirmBtn:
                    confirmBtn.click()
                    confirmBtn = self.driver.find_element_by_id('qr_submit_id')
                return





    def run(self):
        self.wait_input()
        self._login()
        self._order_ticket()


if __name__ == "__main__":
    spider = QiangPiao()
    spider.run()