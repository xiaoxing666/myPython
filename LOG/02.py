# ----需求----
# 1. 所有的日志写到磁盘上
# 2. all.log 文件中记录所有的日志信息
# 3. error.log 文件单独记录 error 以上级别的日志信息
# 4.要求 all.log 在每天凌晨进行日志切割

import logging
import logging.handlers
import datetime

# 定义logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# 为两个不同的文件设置不同的 handler
rf_handler = logging.handlers.TimedRotatingFileHandler('./all.log',when='midnight',interval=1)
rf_handler.setFormatter(logging.Formatter('%(asctime)s----%(levelname)s----%(message)s)'))

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter('%(asctime)s----%(levelname)s----%(message)s)'))

#  把相应的处理器组装到logger
logger.addHandler(rf_handler)
logger.addHandler((f_handler))

# 产生错误日志
logging.debug('一条严重级别为 debug 的日志记录')
logging.info('一条严重级别为 info 的日志记录')
logging.warning('一条严重级别为 warning 的日志记录')
logging.error('一条严重级别为 error 的日志记录')
logging.critical('一条严重级别为 critical 的日志记录')
