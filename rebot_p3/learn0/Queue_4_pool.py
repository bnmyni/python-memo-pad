''' 如果使用到Pool就需要使用到Manager来创建一个Queue否则会报错'''
from multiprocessing import Manager, Pool
import time, os, random

def reader(q):
    while not q.empty():
        print(q.get_nowait())

def writer(q):
    str = 'aspire to Inspire'
    a = list(str)
    for w in a:
        print( 'write---'+ w)
        if not q.full():
            q.put_nowait(w)

if __name__ == "__main__":
    q = Manager().Queue()
    po = Pool()

    po.apply(writer, (q,))
    po.apply(reader, (q,))

    po.close()
    po.join()