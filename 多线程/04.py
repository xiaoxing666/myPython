'''
利用 time 函数,生成两个函数
顺序调用
计算总的运行时间
'''
import time
# 这里不用_thread包,用threading
import threading as thread
def loop(int1):
    print('loop 开始时间:',time.ctime())
    time.sleep(4)
    print ('loop 参数:{0}'.format(int1))
    print('loop 结束时间:',time.ctime())

def loop2(int1,int2):
    print('loop2 开始时间:',time.ctime())
    time.sleep(2)
    print ('loop2 参数:{0},{1}'.format(int1,int2))
    print('loop2 结束时间:',time.ctime())

def main():
    print ('主程序开始时间:',time.ctime())
    # 实例化 thread
    t1 = thread.Thread(target=loop,args=('嘻嘻',))
    t1.start()
    t2 = thread.Thread(target=loop2,args=('嘻嘻','哈哈'))
    t2.start()
    # 等待多线程执行完成
    t1.join()
    t2.join()
    print ('主程序结束时间:',time.ctime())

if __name__ == '__main__':
    main()