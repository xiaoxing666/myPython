import os
import multiprocessing

def info(title):
    print (title)
    print ('module name:',__name__)
    print ('process id:',os.getpid())
    print ('parent process id:',os.getppid())

def f(name):
    info('function f')
    print ('hello',name)

if __name__ == '__main__':
    info('main line')
    p = multiprocessing.Process(target=f,args=('xiaoxin',))
    p.start()
    p.join()