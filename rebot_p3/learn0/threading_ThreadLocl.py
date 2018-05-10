import threading

local_shool = threading.local()

def process_student():
    std = local_shool.student
    print('hello %s (in %s)' % (std, threading.current_thread()))

def process_thread(name):
    local_shool.student = name
    process_student()


if __name__ == "__main__":
    t1 = threading.Thread(target=process_thread, args=('aspire',))
    t2 = threading.Thread(target=process_thread, args=('mayun',))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
