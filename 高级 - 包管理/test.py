
# 导入一个类
'''
import p01 as p

stu = p.Student('xiaoxin',19)
stu.say()

p.sayHello()

# 导入部分内容
from p01 import Student,sayHello
stu = Student()
stu.say()
sayHello()

from p01 import *
stu = Student()
stu.say()
sayHello()

# 可以获取的路径列表
import sys
# 注意:路径的 \ 反斜杠 记得转义
sys.path.append('C:\\Users\\yellow\\Desktop')
print (type(sys.path))
for p in sys.path:
        print (p)

import xxpkg01 as p
ini = p.inInit()

import xxpkg01.p03 as p
stu = p.Student('嘻嘻',3)
stu.say()
'''
from xxpkg02 import *

stu = p01.Student()
stu.say()
inInit()








