from multiprocessing import Process

import os

def run_proc(name):
    print('子进程运行中,进程名称%s,进程id：%s' %  (name, os.getpid()))

if __name__ == '__main__':
    print('父进程id：%s' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('子进程将要执行')
    p.start()
    p.join()
    print('子进程结束')