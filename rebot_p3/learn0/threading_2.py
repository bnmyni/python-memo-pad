''' 多个线程按顺序执行  '''
from threading import  Lock, Thread
import time

def fn1():
    while True:
        if lock1.acquire():
            print('----task1----')
            time.sleep(0.1)
            lock2.release()
def fn2():
    while True:
        if lock2.acquire():
            print('----task2----')
            time.sleep(1)
            lock3.release()

def fn3():
    while True:
        if lock3.acquire():
            print('----task3----')
            time.sleep(1)
            lock1.release()

if __name__ == "__main__":
    lock1 = Lock()
    lock2 = Lock()
    lock3 = Lock()

    lock2.acquire()
    lock3.acquire()

    f1 = Thread(target=fn1)
    f2 = Thread(target=fn2)
    f3 = Thread(target=fn3)

    f1.start()
    f2.start()
    f3.start()
