# -*- coding: utf-8 -*-
'''
使用内建的isinstance函数可以判断一个变量是不是字符串
'''
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
