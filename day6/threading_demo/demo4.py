import threading

#解决共享变量的安全问题
VALUES = 0

gLock = threading.Lock()
def add_value():
    global VALUES
    gLock.acquire() #开始访问变量的时候 上锁
    for x in range(1000000):
        VALUES +=1
    gLock.release() #线程处理完毕 释放锁
    print("value:%d" % VALUES)

def main():
    for x in range(2):
        t = threading.Thread(target=add_value)
        t.start()

if __name__ == "__main__":
    main()