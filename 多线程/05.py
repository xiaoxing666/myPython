import time
import threading as thread

#  非守护线程
def fun():
    print ('函数开始运行!')
    time.sleep(2)
    print ('函数结束啦!')

print ('主线程开始运行!')

t1 = thread.Thread(target=fun,args=())
t1.start()

time.sleep(1)
print("主线程结束啦!")