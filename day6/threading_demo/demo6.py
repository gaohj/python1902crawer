#生产者 和 消费者
#生产者 的线程专门用来产生数据   存到中间变量中
#消费者从中间变量中 取出数据 进行消费
#中间 变量 作为全局变量
#需要使用锁 保证全局变量的完整性
import random
import threading
import time
gCondition = threading.Condition()
gMoney = 1000
gTotalTime = 30  #规定次数
gTime = 0


class ProducerThread(threading.Thread):
    def run(self):
        global gMoney
        global gTime
        while True:
            money = random.randint(99,999) #产生随机整型值 每次挣的钱
            gCondition.acquire() #操作全局变量 上锁
            if gTime >= gTotalTime:
                gCondition.release()
                break
            gMoney += money  #修改全局变量
            print("%s生产了%d元钱,余额为%d元" %(threading.current_thread(),money,gMoney))

            gTime += 1
            gCondition.notify_all()#通知所有正在等待的线程
            gCondition.release()  #线程结束  释放锁
            time.sleep(1)

class CustomerThread(threading.Thread):
    def run(self):
        global gMoney
        while True: #死循环
            money = random.randint(99,999) #随机花费的钱
            gCondition.acquire() #上锁
            while gMoney < money:
                #if 判断完了之后立即执行  下面的语句
                #while 执行完了以后回来再判断一次
                #避免了 等待有钱以后去消费 发现还是余额不足
                if gTime >= gTotalTime:
                    gCondition.release()#超过了10次
                    return #用return 替换 break 目的是 return 返回所有
                print("%s准备消费%d元钱,余额为%d元,余额不足" % (threading.current_thread(), money, gMoney))
                gCondition.wait() #如果余额不足  等待 notify_all 的通知
            gMoney -= money
            print("%s消费了%d元钱,余额为%d元" % (threading.current_thread(), money, gMoney))
            gCondition.release()
            time.sleep(1)


def main():
    for x in range(3):
        t = ProducerThread()
        t.start()
    for x in range(3):
        t = CustomerThread()
        t.start()

if __name__ == "__main__":
    main()