import os

## fork()无法在windows上面运行
rpid = os.fork()

if rpid < 0:
    print('fork 失败')
elif rpid ==0:
    print('子进程id:%s;父进程id:%s' % (os.getpid(), os.getppid()))
else:
    print('子进程id:%s;父进程id:%s' % (rpid, os.getpid()))

print('主进程.....')