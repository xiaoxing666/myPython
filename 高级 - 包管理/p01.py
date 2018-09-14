# 包含一个学生类,一个 sayHello 函数,一个打印语句

class Student():

    def __init__(self,name='wan',age=23):

        self.name = name
        self.age = age

    def say(self):
        print("my name is {0}".format(self.name))
        print("i am {0} years old".format(self.age))
def sayHello():
    print ('Hello,我是模块p01')

# 判断语句 建议作为程序的入口
if __name__ == '__main__':
    print ('欢迎来到我的这个文件!')