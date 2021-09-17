import threading

class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global data
        dataLock.acquire()
        data += 5
        print(data)
        dataLock.release()

data = 10
dataLock = threading.Lock()

a = MyThread()
a.start()

b = MyThread()
b.start()