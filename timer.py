from datetime import datetime
import sms

from apscheduler.schedulers.blocking import BlockingScheduler


def job_function():
    try:
        sms.task()
        print("done successfully")
    except:
        print("Something went wrong")

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(job_function, 'interval', seconds=10)

sched.start()