#encoding:utf-8
import time
import threading
# def eat():
#     for x in range(3):
#         print("正在吃鸡%s" % x)
#         time.sleep(1)
#
# def drink():
#     for x in range(3):
#         print("正在今朝醉%s" % x)
#         time.sleep(1)

#以上是传统的方式  6秒

def eat():
    for x in range(3):
        print("正在吃鸡%s" % threading.current_thread())
        time.sleep(1)

def drink():
    for x in range(3):
        print("正在今朝醉%s" % threading.current_thread())
        time.sleep(1)

def main():
    t1 = threading.Thread(target=eat)
    t2 = threading.Thread(target=drink)

    t1.start()
    t2.start()

if __name__ == "__main__":
    main() #只需要3秒 



