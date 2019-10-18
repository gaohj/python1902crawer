test = ['zhangsan','lisi','wangwu','zhaoliu']
print(test)#['zhangsan', 'lisi', 'wangwu', 'zhaoliu']
print(list(enumerate(test)))
#[(0, 'zhangsan'), (1, 'lisi'), (2, 'wangwu'), (3, 'zhaoliu')]
print(list(enumerate(test,start=1)))