'''
利用 time 函数,生成两个函数
顺序调用
计算总的运行时间
'''
import time

def loop():
    print('loop1 开始时间:',time.ctime())
    time.sleep(4)
    print('loop1 结束时间:',time.ctime())

def loop2():
    print('loop2 开始时间:',time.ctime())
    time.sleep(2)
    print('loop2 结束时间:',time.ctime())

def main():
    print ('主程序开始时间:',time.ctime())
    loop()
    loop2()
    print ('主程序结束时间:',time.ctime())

if __name__ == '__main__':
    main()