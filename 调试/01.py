def sayHello(name):
    print ('hello,{0}'.format(name))

if __name__ == '__main__':
    name = input('请输入您的姓名:')
    sayHello(name=name)
    sayHello(name=name)