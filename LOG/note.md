#  LOG
- logging 
- logging 模块提供模块级别的函数记录日志
- 包括四大组件

## 1.日志相关概念
- 日志
- 日志的级别 (level)
    - 不同的用户关注不同的程序信息
    - 登记从上到下,越来越高
    - DEBUG
    - INFO
    - NOTICE
    - WARNING
    - ERROR
    - CRITICAL
    - ALERT
    - EMERGENCY
- IO 操作 => 不要频繁操作
- LOG的作用
    - 调试
    - 了解软件的运行情况
    - 分析定位问题
- 日志信息
    - time
    - 地点
    - level
    - 内容
- 成熟的第三方日志
    - log4j
    - log4php
    - logging
# 2 Logging模块
- 日志级别
    - 级别可以自定义
    - DEBUG
    - INFO
    - WARNING
    - ERROR
    - CRITICAL
- 初始化/写日志实例需要指定级别,只有当级别等于或者指定级别才别记录
- 使用方式
    - 直接使用 logging (封装了其他组件)
    - logging 四大组件直接定制
## 2.1 logging模块级别的日志
- 使用一下几个函数
    - logging.debug(msg,*args,**kwargs) 创建一条严重级别为 debug 的日志记录
    - logging.info(msg,*args,**kwargs) 创建一条严重级别为 info 的日志记录
    - logging.warning(msg,*args,**kwargs) 创建一条严重级别为 warning 的日志记录
    - logging.error(msg,*args,**kwargs) 创建一条严重级别为 error 的日志记录
    - logging.critical(msg,*args,**kwargs) 创建一条严重级别为 critical 的日志记录
    - logging.log(level,*args,**kwargs) 创建一条严重级别为 level 的日志记录
    - logging.basicConfig(**kwargs) 对 root logger 进行一次性配置
    
- logging.basicConfig(**kwargs) 
    - 只在第一次调用的时候起作用
    - 不配置 logger 则使用默认值 WARNING
        - 输出: sys.stderr
        - 级别: WARNING
        - 格式: level:log_name:content
- 示例 01.py
- format 参数
        
        %(name)s Logger的名字
        %(levelname)s 文本形式的日志级别
        %(message)s 用户输出的消息
        %(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
        %(levelno)s 数字形式的日志级别
        %(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
        %(filename)s 调用日志输出函数的模块的文件名
        %(module)s  调用日志输出函数的模块名
        %(funcName)s 调用日志输出函数的函数名
        %(lineno)d 调用日志输出函数的语句所在的代码行
        %(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
        %(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
        %(thread)d 线程ID。可能没有
        %(threadName)s 线程名。可能没有
        %(process)d 进程ID。可能没有
        
## 2.2 logging 模块的处理流程
- 四大组件
    - 日志器(Logger):产生日志的一个接口
    - 处理器(Handler):把产生的日志发送到相应的目的地
    - 过滤器(Filter):更精细地控制哪些日志输出
    - 格式器(Formatter):对输出信息进行格式化
- Logger
    - 产生一个日志
    - 操作
            
            Logger.setLevel() 设置日志器将会处理的日志消息的最低严重级别
            Logger.addHander() 和 Logger.removeHandler 为该logger对象添加和移除一个处理器
            Logger.addFilter() Logger.removerFilter
            Logger.debug() 产生一条 debug 级别的日志
            Logger.exception()
            Logger.log() 获取一个明确的日志 level 参数类创建一个日志记录
    - 如何得到一个 logger 对象:
        - 实例化
        - logging.getLogger()
            
- Handler
    - 把 log 发送到指定位置
    - 方法
        - setLevel
        - setFormat
        - addFilter , removeFilter
    - 不需要直接使用,Handler 是基类
            
            logging.StreamHandler 
            logging.FileHandler
            logging.handlers.RotatingFileHandler 循环日志文件
            logging.handlers.TimedRotatingFileHandler 定时循环日志handler
            logging.handlers.HTTPHandler
            logging.handlers.SMTPHandlers
            logging.NullHandler 空操作handler
- Format 类
    - 直接实例化
    - 可以继承Format添加特殊内容
    - 三个参数 
        - fmt : 指定消息格式化字符串,如果不指定该参数则默认使用 message 的原始值
        - datefmt : 指定日期格式字符串,默认"%Y-%m-%d %H:%M:%S"
        - style : python 3.2新增的参数,可取值为 % { $ ,默认 $     
- Filter 类
    - 可以被 Handler 和 Logger 使用
    - 控制传递过来的消息的具体内容
    - 示例 02.py

