import time
import threading as thread

#  守护线程
def fun():
    print ('函数开始运行!')
    time.sleep(2)
    print ('函数结束啦!')

print ('主线程开始运行!')

t1 = thread.Thread(target=fun,args=())

# 守护线程必须在启动前设置!!
t1.setDaemon(True)
t1.start()

# 主线程休息一秒钟,函数休息2秒钟,设置了守护线程1秒后等不到函数运行就直接结束
time.sleep(1)
print("主线程结束啦!")
