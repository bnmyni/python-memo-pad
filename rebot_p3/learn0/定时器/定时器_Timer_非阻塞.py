from threading import Timer
import time

def worker(msg):
    print('%s任务开始执行，执行时间%s' % (msg, time.time()))


if __name__ == "__main__":
    print('startime : %s' % time.time())
    t = Timer(2, worker, ('考核', ))
    t.start()
    print('endtime : %s' % time.time())