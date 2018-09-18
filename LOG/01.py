import logging

# 注意注意: 不配置 logger 则使用默认值 WARNING,所以debug和info就不会被输出/保存
logging.basicConfig(filename='./01.log',level=logging.DEBUG)

# LOG FORMAT = "%(asctime)s----%(levelname)s----%(message)s"
# 按照格式输出到文件,但是此处写得也有问题,怎么处理?

# 第一种写法
logging.debug('一条严重级别为 debug 的日志记录')
logging.info('一条严重级别为 info 的日志记录')
logging.warning('一条严重级别为 warning 的日志记录')
logging.error('一条严重级别为 error 的日志记录')
logging.critical('一条严重级别为 critical 的日志记录')

#logging.basicConfig(**kwargs) #对 root logger 进行一次性配置

# 另外一种写法
#logging.log(level,*args,**kwargs) #创建一条严重级别为 level 的日志记录
logging.log(logging.DEBUG,'一条严重级别为 debug 的日志记录')
logging.log(logging.INFO,'一条严重级别为 info 的日志记录')
logging.log(logging.WARNING,'一条严重级别为 warning 的日志记录')
logging.log(logging.ERROR,'一条严重级别为 error 的日志记录')
logging.log(logging.CRITICAL,'一条严重级别为 critical 的日志记录')

