import threading
import time
import random

def producer():
    while True:
        condition.acquire()
        if len(data) >= 5:
            print('producer is waiting...')
            condition.wait()
        else:
            data.append(random.randint(1,100))
            print('product left:         ',data)
            print(c.is_alive())
            time.sleep(1)
        condition.notify()
        condition.release()

def consumer():
    while True:
        condition.acquire()
        if not data:
            print('consumer waiting...')
            condition.wait()
        else:
            print('consumer took away:', data.pop(0))
            print('product left:     :', data)
            print(c.is_alive())
            time.sleep(1)
        condition.notify()
        condition.release()

condition = threading.Condition()
data = []

p = threading.Thread(name='producer', target=producer)
c = threading.Thread(name='consumer',target=consumer)

p.start()
c.start()

p.join()
c.join()
