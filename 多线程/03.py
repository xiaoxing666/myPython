'''
利用 time 函数,生成两个函数
顺序调用
计算总的运行时间
'''
import time
# _thread 是老的多线程包,建议用 threading
import _thread as thread
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
    # 启动多线程 start_new_thread
    # 两个参数,第一个需要运行的函数名,第二个是函数的参数作为元祖使用
    # 如果只有一个参数,后面加一个逗号
    thread.start_new_thread(loop,('嘻嘻',))
    thread.start_new_thread(loop2,('嘻嘻','哈哈'))
    print ('主程序结束时间:',time.ctime())

if __name__ == '__main__':
    main()
    # 等待多线程执行完成
    # 不加下面这个就没有结束,重点注意!!!
    while True:
        time.sleep(1)