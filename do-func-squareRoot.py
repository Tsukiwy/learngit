# -*- coding: utf-8 -*-
'''
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程:
ax2 + bx + c = 0 的两个解。
提示：计算平方根可以调用math.sqrt()函数：
'''

'''
知识点：
# isinstance (a,(str,int,list))    是元组中的一个返回 True
# raise Exception("Invalid level!", level)
# 触发异常后，后面的代码就不会再执行
'''

import math
def quadratic(a,b,c):
    if not isinstance(a,(int,float)):   
        raise TypeError('a is not a number')
    if not isinstance(b,(int,float)):
        raise TypeError('b is not a number')
    if not isinstance(c,(int,float)):
        raise TypeError('c is not a number')
    d=b*b-4*a*c
    if a==0:
        if b==0:
            if c==0:
                return '方程根为全体实数'
            else:
                return '方程无根'
        else:
            x1=-c/b
            x2=x1
            return x1,x2
    else:
        if d<0:
            return '方程无根'
        else:
            x1 = (-b + math.sqrt(d))/2/a 
            x2 = (-b - math.sqrt(d))/2/a
            return x1,x2        
print(quadratic(2,3,1))
print(quadratic(1,3,-4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

