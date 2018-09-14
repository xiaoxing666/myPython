# 1.  模块
- 一个模块就是一个包含 python 代码的文件,后缀名是 .py 就可以,模块就是个 python 文件
- 为什么我们用模块
    - 程序太大,编写维护非常不方便,需要拆分
    - 模块可以增加代码重复利用的方式
    - 当做命名空间使用,避免命名冲突
- 如何定义模块
    - 模块就是一个普通文件,所以任何代码可以直接书写
    - 不过根据模块的而规范,最好在模块中编写一下内容
        - 函数(单一功能)
        - 类(相似功能的组合,或者相似业务模块)
        - 测试代码

- 如何使用模块
    - 模块直接导入
        - 假如模块名称直接以数字开头,借助于importlib包可以实现导入以数字开头的模块名称
               
                import importlib
                var = importlib.import_module('01')
                
    - 语法
        - import modul_name
        - module_name.function_name
        - module_name.class_name
    - import 模块 as 别名
        - 导入的同时给模块起一个别名
        - 其余用法相同
        
    - from module_name import func_name,class_name
        - 有选择性导入
        - 使用的时候可以直接使用导入的内容
        
    - from module_name import *
        - 优点:对比直接 import module_name 调用的时候省了个 module_name 前缀
        - 缺点:和其他模块一起导入时,可能会出现重名现象
    - if __name__ == '__main__': 的使用
        - 可以有效避免模块代码被导入的时候被动执行的问题
        - 建议所有程序的入口都以此代码为入口
        
# 2.  模块的搜索路径和存储
- 什么是模块的搜索路径:
    - 加载模块的时候,系统会在哪些地方寻找此模块
- 系统默认的模块搜索路径
    
        import sys
        sys.path 属性可以获取路径列表
- 添加搜索路径

        sys.path.append(dir) 注意:路径的 \ 反斜杠 记得转义
        
- 模块的加载顺序
    - 1.先搜索内存中已经加载好的模块
    - 2.搜索 python 的内置模块
    - 3.搜索 sys.path 路径
    
# 3.  包
- 包是一种组织管理代码的方式,包里面存放的是模块
- 用于将模块包含在一起的文件夹就是包

        /---包
        /---/--- __init__.py 包的标志文件
        /---/--- 模块1
        /---/--- 模块2
        /---/--- 子包(子文件夹)
        /---/---/--- __init__.py 子包的标志文件
        /---/---/--- 子包模块1
        /---/---/--- 子包模块2    
        
- 包的导入操作
    - import package_name
        - 直接导入一个包,可以使用__init__.py中的内容
        - 使用方式是:
        
                package_name.func_name
                package_name.class_name.func_name
    
    - import package_name sa p
        - 用法跟导入模块类似
        - 注意的是此种方法默认对 __init__.py 内容的导入
    
    - import package_name.module_name as m
        - 导入包中某一个具体的模块
        - 使用方法
        
                package_name.module_name.func_name
                package_name.module_name.class_name.fun_name
                package_name.module_name.class_name.var            
        
    - from ... improt 导入
        - from package_name import module_name
        - 此中导入方法不执行 __init__ 的内容    
    
                form xxpkg01 import p03
                p03.sayHello()
                
        - from xxpkg01 import *
            - 只导入当前包 __init__.py 文件中所有的函数和类
            
    - from package_name.module_name import *
        - 导入包中指定的模块中所有内容
    - 在开发环境中经常会用其他模块,可以在当前包中直接导入其他模块中的内容
        - import 完整的包或者模块的路径
    - '__all__' 方法的用法
        - 在使用 from package_name import * 的时候,* 可以导入的内容
        - __init__.py 文件如果为空,或者没有 __all__ ,那么只可以把 __init__ 的内容导入
        - __init__ 如果设置了 __all__ 的值,那么则按照 __all__ 指定的包或者模块进行导入,这样就不会导入 __init__ 的内容
        - __all__ = ['module_name1','module_name2','package1....']
    
# 3.  命名空间
- 用于区分不同位置不同功能但和名字相同的函数或者变量的一个特定前缀
- 作用是防止名字冲突

            
    
    
    
    
    
    
    
    