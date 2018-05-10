'''
使用sched进行延迟处理定时器
'''
import time
import sched

def worker(msg, starttime):
    print('%s任务开始执行，执行时间%s' % (msg, time.time()))


if __name__ == "__main__":
    s = sched.scheduler(time.time, time.sleep)
    print('startime : %s' % time.time())
    s.enter(7, 1, worker, ('考核', time.time()))
    s.enter(5, 1, worker, ('邮件发送', time.time()))
    s.run()
    print('endtime : %s' % time.time())