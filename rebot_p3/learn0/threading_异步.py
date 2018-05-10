from multiprocessing import Pool
import time
import os

def test():
    print('start test,when test end callback test1()')
    for i in range(3):
        print('test print %d' % i)
        time.sleep(1)
    return 'aspire'

def test1(args):
    print('if start test1, func test end now')
    print('test return : %s' % args)

if __name__ == "__main__":
    pool = Pool(3)
    pool.apply_async(func=test,callback=test1)
    time.sleep(5)
    print('main pid %s' % os.getpid())