import threading
import time


def sing():
    for i in range(5):
        print('sing %d' % i)
        time.sleep(1)

def dance():
    for i in range(4):
        print('dance %d' % i)
        time.sleep(1)

if __name__ == "__main__":
    t = threading.Thread(target=sing)
    t1 = threading.Thread(target=dance)
    t.start()
    t1.start()

    while True:
        ## 获取当前线程数量
        lens = len(threading.enumerate())
        print('当前线程数%d' % lens)

        if lens <= 1:
            break
        time.sleep(0.5)