import threading
import time

loop= [4,2]
class ThreadFunc:

    def __init__(self,name):
        self.name = name

    def loop(self,nloop,nsec):
        '''
        :param nloop: loop 函数的名称
        :param nsec: 系统休眠时间
        :return:
        '''
        print ('{0}开始运行,时间:{1}'.format(nloop,time.ctime()))
        time.sleep(nsec)
        print ('{0}结束运行,时间:{1}'.format(nloop,time.ctime()))

def main():
    print ('主线程开始时间:{0}'.format(time.ctime()))
    t_f1 = ThreadFunc('loop1')
    t1 = threading.Thread(target=t_f1.loop, args=("LOOP1",4))
    t_f2 = ThreadFunc('loop2')
    t2 = threading.Thread(target=t_f2.loop, args=("LOOP2",2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()


if __name__ == '__main__':
    main()
