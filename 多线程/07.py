import time
import threading as thread

def loop1():
    print('loop1 开始时间:',time.ctime())
    time.sleep(4)
    print('loop1 结束时间:',time.ctime())

def loop2():
    print('loop2 开始时间:',time.ctime())
    time.sleep(2)
    print('loop2 结束时间:',time.ctime())

def loop3():
    print('loop3 开始时间:',time.ctime())
    time.sleep(5)
    print('loop3 结束时间:',time.ctime())

def main():
    print ('主程序开始时间:',time.ctime())
    t1 = thread.Thread(target=loop1, args=())
    # 给 t1 设置一个线程名字
    t1.setName('THR_1')
    t1.start()

    t2 = thread.Thread(target=loop2, args=())
    # 给 t1 设置一个线程名字
    t2.setName('THR_2')
    t2.start()

    t3 = thread.Thread(target=loop3, args=())
    # 给 t1 设置一个线程名字
    t3.setName('THR_3')
    t3.start()

    # 等待多线程执行完成
    # loop2 睡2秒,预计三秒后 THR_2 在主程序结束前自动结束
    time.sleep(3)
    for thr in thread.enumerate():
        print ('当前还在运行的线程名字有:',thr.getName())
    # debug 模式下测试,有6个线程
    # run 模式下测试,有3个线程
    print ('当前还在运行的子线程数量为:',thread.activeCount())
    print ('主程序结束时间:',time.ctime())


if __name__ == '__main__':
    main()