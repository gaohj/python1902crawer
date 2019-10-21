import threading

VALUES = 0
def add_value():
    global VALUES
    for x in range(1000000):
        VALUES +=1
    print("value:%d" % VALUES)

def main():
    for x in range(2):
        t = threading.Thread(target=add_value)
        t.start()

if __name__ == "__main__":
    main()
    #value:1185975
    #value:1280472