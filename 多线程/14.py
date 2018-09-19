import threading
import time

lock_1 = threading.Lock()
lock_2 = threading.Lock()

def fun_1():
    print ('fun_1()开始')
    lock_1.acquire(timeout=4)
    print('fun_1()申请了 lock_1')
    time.sleep(2)
    print ('fun_1() 等待 lock_2')
    result = lock_2.acquire(timeout=2)
    if result:
        print ('fun_1 得到了 lock_2')
        lock_2.release()
        print('fun_1 释放了锁 lock_2')
    else:
        print ('fun_1 没申请到 lock_2')
    lock_1.release()
    print ('fun_1() 释放了 lock_1')
    print('fun_1程序运行结束')

def fun_2():
    print ('fun_2()开始')
    lock_2.acquire()
    print('fun_2()申请了 lock_2')
    time.sleep(4)
    print ('fun_2() 等待 lock_1')
    lock_1.acquire()
    print('fun_2()申请了 lock_1')
    lock_1.release()
    print('fun_2()释放了 lock_1')
    lock_2.release()
    print ('fun_2() 释放了 lock_2')
    print('fun_2程序运行结束')

if __name__ == '__main__':
    t1 = threading.Thread(target=fun_1,args=())
    t2 = threading.Thread(target=fun_2, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # 产生死锁