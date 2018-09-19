import threading
import time

def fun():
    print ('我在运行中...')
    time.sleep(3)
    print('程序结束结束')

if __name__ == '__main__':
    t = threading.Timer(6,fun)
    t.start()

    i = 0
    while True:
        print ('********',i)
        time.sleep(3)
        i += 1