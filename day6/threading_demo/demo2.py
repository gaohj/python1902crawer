import time
import threading

class EatThread(threading.Thread):
    def run(self):
        for x in range(3):
            print("正在吃鸡 %s " % threading.current_thread())
            time.sleep(1)


class DrinkThread(threading.Thread):
    def run(self):
        for x in range(3):
            print("正在喝酒 %s " % threading.current_thread())
            time.sleep(1)

def main():
    t1 = EatThread()
    t2 = DrinkThread()

    t1.start()
    t2.start()

if __name__ == "__main__":
    main()