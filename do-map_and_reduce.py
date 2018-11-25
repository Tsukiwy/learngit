# -*- coding: utf-8 -*-
'''
利用map和reduce编写一个str2float函数，把字符串'12.34567'转换成浮点数12.34567：
'''

from functools import reduce
def str2float(s):
   def fn(x, y):
        return x * 10 + y
   def char2num(s):
         return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
   return reduce(fn, map(char2num, s.replace(".","")))
s="12.34567"
if s.find(".")!=-1:
     print('str2float(\'%s\') ='%s, str2float(s)/pow(10,(len(s)-s.find(".")-1)))
     print(len(s),s.find("."))   #8 2
else:
     print('str2float(\'%s\') ='%s, str2float(s))