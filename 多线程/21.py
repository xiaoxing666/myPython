import multiprocessing
import time


def producer(sequence,output_q):
    print ('生产时间:',time.ctime())
    for item in sequence:
        output_q.put(item)
        print ('put',item,'into q')
    print('生产结束:',time.ctime())

def consumer(input_q):
    print ('消费时间:',time.ctime())
    while True:
        item = input_q.get()
        print ('pull',item,'out of q')
    print ('完成时间',time.ctime())

if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    cons_p = multiprocessing.Process(target=consumer,args=(q,))
    cons_p.deamon = True
    cons_p.start()

    sequence = [1,2,3,4]
    producer(sequence,q)
    q.join()