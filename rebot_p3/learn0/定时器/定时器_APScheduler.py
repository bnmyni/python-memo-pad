from apscheduler.schedulers.blocking import  BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

sched = BlockingScheduler()

def worker():
    print('-'* 30)

@sched.scheduled_job('cron', day_of_week='*', hour='10', minute=49, second=30)
def cron_worker():
    print('cron worker running now...')

sched.add_job(worker, IntervalTrigger(weeks=0,days=0,hours=0,minutes=0,seconds=5))
sched.start()
sched.shutdown(wait=False)
