import multiprocessing
import  time
def clock(interval):
    while True:
        print ('现在的时间是:',time.ctime())
        time.sleep(interval)

if __name__ == '__main__':
    p = multiprocessing.Process(target=clock,args=(5,))
    p.start()
    p.join(4)

