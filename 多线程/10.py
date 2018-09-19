import threading

sum = 0
loopSum = 1000000

def myAdd():
    global sum,loopSum
    for i in range(1,loopSum):
        sum += 1

def myMiun():
    global sum,loopSum
    for i in range(1,loopSum):
        sum -= 1

if __name__ == '__main__':
    print ("开始计算{0}".format(sum))
    t1 = threading.Thread(target=myAdd,args=())
    t2 = threading.Thread(target=myMiun, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("计算结束:sum={0}".format(sum))