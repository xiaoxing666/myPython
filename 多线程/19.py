import multiprocessing
import  time

class clockProcess(multiprocessing.Process):

    def __init__(self,interval):
        super().__init__()
        self.interval = interval

    def run(self):
        while True:
            print ('当前时间',time.ctime())
            time.sleep(self.interval)

if __name__ == '__main__':
    p = clockProcess(2)
    p.start()