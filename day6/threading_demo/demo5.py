#生产者 和 消费者
#生产者 的线程专门用来产生数据   存到中间变量中
#消费者从中间变量中 取出数据 进行消费
#中间 变量 作为全局变量
#需要使用锁 保证全局变量的完整性
import random
import threading
import time
gLock = threading.Lock()
gMoney = 1000
gTotalTime = 10  #规定次数
gTime = 0


class ProducerThread(threading.Thread):
    def run(self):
        global gMoney
        global gTime
        while True:
            money = random.randint(99,999) #产生随机整型值 每次挣的钱
            gLock.acquire() #操作全局变量前获取锁 上锁
            if gTime >= gTotalTime:
                gLock.release()
                break
            gMoney += money  #修改全局变量
            print("%s生产了%d元钱,余额为%d元" %(threading.current_thread(),money,gMoney))
            gTime += 1
            gLock.release()  #线程结束  释放锁
            time.sleep(1)

class CustomerThread(threading.Thread):
    def run(self):
        global gMoney
        while True:
            money = random.randint(99,999) #随机花费的钱
            gLock.acquire()
            if gMoney>= money:
                gMoney -= money
                print("%s消费了%d元钱,余额为%d元" % (threading.current_thread(), money, gMoney))
            else:
                if gTime >= gTotalTime:
                    gLock.release()
                    break #虽然这里break 跳出循环  但是锁并没有完全释放 导致锁一致在等待
                print("%s准备消费%d元钱,余额为%d元,余额不足" % (threading.current_thread(), money, gMoney))
            gLock.release()
            time.sleep(1)


def main():
    for x in range(5):
        t = ProducerThread()
        t.start()
    for x in range(3):
        t = CustomerThread()
        t.start()

if __name__ == "__main__":
    main()