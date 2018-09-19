import threading
import time

semaphore = threading.Semaphore(3)

def fun():
    if semaphore.acquire():
        for i in range(5):
            print(threading.currentThread().getName()+' get semaphore')
        time.sleep(10)
        semaphore.release()
        print(threading.currentThread().getName()+' release semaphore')

for i in range(8):
    t1 = threading.Thread(target=fun)
    t1.start()