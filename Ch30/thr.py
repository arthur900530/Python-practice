import threading
import time

def wake():
    print(threading.current_thread().getName(),' starting')
    time.sleep(10)
    print('WAKE UP!')
    print(threading.current_thread().getName(),' exit')

thread1 = threading.Thread(name='daemon',target=wake)
thread1.setDaemon(False)
thread1.start()
thread1.join(1)
print(threading.current_thread().getName())
for i in range(1,6):
    print(i)
    time.sleep(1)
print(threading.active_count())
print(threading.enumerate())
# print(thread1.is_alive())