from queue import Queue
import threading
import time

# q = Queue(4)
# # q.put(1)
# for x in range(4):
#     q.put(x)
# # print(q.qsize()) 队列大小
# # print(q.full()) 是否满了
# # print(q.empty()) 是否为空
# for x in range(4):
#     print(q.get())

#往队列中存数据
def set_value(q):
    index = 0
    while True:  #一直放进去
        q.put(index)  #如果满了 处于阻塞状态
        index +=1
        time.sleep(3)

#从队列中取数据
def get_value(q):
    while True:
        print(q.get()) #如果为空 也是处于阻塞状态
        time.sleep(5)

def main():
    q = Queue(4)
    t1 = threading.Thread(target=set_value,args=[q])
    t2 = threading.Thread(target=get_value,args=[q])

    t1.start()
    t2.start()

if __name__ == "__main__":
    main()