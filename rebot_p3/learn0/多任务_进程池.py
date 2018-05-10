# encoding=utf-8
from multiprocessing import Pool
import os, time, random

def worker(msg):
    t_start = time.time()
    print("%s开始执行,进程号%d" % (msg, os.getpid()))
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg, "执行完成，耗时%0.2f" % (t_stop - t_start))

## 这个是必须要加的，否则会报错
if __name__ == '__main__':
    #
    po = Pool(3)
    #
    for i in range(0, 10):
        po.apply_async(func=worker, args=(i,))
        # po.apply(worker(i), (i, ))
    #
    ##  关闭，进程池不再接受新的请求
    po.close()
    # ## 等待所有的进程接受，必须在close之后
    po.join()
