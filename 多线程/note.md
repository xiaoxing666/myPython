# 环境
- Ubuntu 16.04
- anaconda
- pycharm
- python 3.6

# 多线程 vs 多进程
- 程序: 一堆代码以文本形式存入一个文档
- 进程: 程序运行的一个状态
    - 包含地址空间,内存,数据栈等
    - 每个进程有自己完全独立的运行环境,多进程共享数据是一个问题
- 线程
    - 一个进程的独立运行片段,一个进程可以有多个线程
    - 轻量化的进程
    - 一个进程的多个线程间共享数据和上下文运行环境
    - 共享互斥问题
- 全局解释器锁(GIL)
    - Python 代码的执行是由 python 虚拟机进行控制
    - 在主循环中只能有一个控制线程在执行
- python 包
    - thread : 有问题,不好用,python3 改成了_thread
    - threading :通行的包
- 示例 01.py    

- threading 的使用
    - 直接利用 threading.Thread 生成 Thread 实例
        - 1 t = threading.Thread(target=fun_name,args=(xxx,xxx))
        - 2 t.start()   启动多线程
        - 3 t.join()    等待多线程执行完成
        - 守护线程 - deamon
            - 如果在程序中将子线程设置成守护线程,则子线程会在主线程结束的时候自动退出
            - 一般认为,守护线程不重要或者不允许离开主线程独立运行
            - 守护线程案例能否有效果跟环境有关
            - 05.py 非守护线程
            - 06.py 守护线程
        - 线程常用方法
            - threading.currentThread() 返回当前线程变量
            - threading.enumerate() 返回一个包含现在正在运行的现成的list
            - thread.activeCount() 返回正在运行的线程数列
            - t1.getName() 实例化对象设置线程名字
            - t1.setName() 得到实例化对象线程名字
            - 07.py
    - 直接继承自 threading.Thread
        - 直接继承 Thread
        - 重写 run 函数
        - 类实例可以直接运行
        - 08.py        
        - 09.py 工业风案例
- 共享变量
    - 共享变量 : 当多个线程同时访问同一个变量的时候,会产生共享变量的问题
    - 10.py
    - 解决办法 : 锁 信号灯 
    - 锁 LOCK
        - 是一个标准,表示一个线程在占用一些资源
            - 上锁
            - 使用共享资源
            - 取消锁,释放锁
        - 11.py
        - 锁谁 : 哪个资源需要多个线程共享
        - 理解锁 : 锁其实不是锁住谁,而是一个令牌
    - 线程安全问题
        - 如果一个资源/变量,对于多线程不用加锁也不用引起任何问题,则称为线程安全
        - 线程不安全变量类型 : list set dict (加锁)
        - 线程安全变量类型 : queue 队列
    - 生产者消费者问题
        - 一个模型,可以用来搭建消息队列
        - queue 是存放变量的数据结构,特点是先进先出,内部元素排队
        - 12.py
    - 死锁问题  13.py
    - 锁的等待时间问题 14.py
    - semaphore 
        - 允许一个资源最多有几个多线程同时使用
        - 15.py
    - threading.Timer
        - 16.py  
        - Timer 是利用多线程,在制定时间后启动一个功能  
    - 可重入锁
        - 一个锁,可以被一个线程多次申请
        - 主要解决递归调用的时候,需要申请锁的情况
        - 17.py
    
# 线程替代方案
- subprocess
    - 完全跳过线程,使用进程
    - 是派生进程的主要替代方案
    - python 2.4后引入
- multiprocessing
    - 使用 threading 接口派生,使用子进程
    - 允许为多核或者多 cpu 派生进程,接口跟 threading 非常相似
    - python 2.6 引入
- concurrent.futures
    - 新的异步执行模块
    - 任务级别的操作
    - python 3.2 后引入
# 多进程
- 进程间通讯(InterprocessCommunication,IPC)
- 进程之间无任何共享状态
- 进程的创建
    - 直接生成 Process 实例对象 18.py
    - 派生用法    19.py
    
- 在OS中查看 pid, ppid 以及他们的关系(process id,parent process id)
    - 20.py
- 生产者消费者模型
    - JoinableQueue
    - 21.py 
    - 队列中哨兵的使用 22.py
    
    
    
    