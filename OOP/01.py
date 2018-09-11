
'''
定义一个学生类,用来形容学生
'''
# 定义一个空的类
class Student():
    # 一个空类 ,pass 代表直接跳过
    # 此处 pass 必须有
     pass

# 定义一个对象
stu1 = Student()

# 再定义一个类,用来描述听 python 的学生

class PythonStudent():
    # 用 None 给不确定的属性赋值
    name = None
    age = 21
    course = "Python"


    # 需要注意
    # 1. def doHomework 的缩进层级
    # 2. 系统默认出一个 self 参数
    def doHomeWork(self):
        print ('我在做作业!')
        # 推荐在函数末尾使用 return
        return None

# 示例化一个对象
xiaoxin = PythonStudent()
xiaoxin.doHomeWork()
print (xiaoxin.age)
print (xiaoxin.name)
print (xiaoxin.course)
# 注意成员函数的调用没有传递进入的参数 (self)


#




