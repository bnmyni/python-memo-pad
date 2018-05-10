''' 运用queue两个进程之间边读边写 '''
from multiprocessing import Queue
from multiprocessing import Process
def read(q):
    while not q.empty():
        print(q.get_nowait())

def write(q):
    str = 'aspire to Inspire'
    a = list(str)
    for w in a:
        print( 'write---'+ w)
        if not q.full():
            q.put_nowait(w)

if __name__ == "__main__":
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pw.join()

    pr.start()
    pr.join()
    print('--'* 15)


