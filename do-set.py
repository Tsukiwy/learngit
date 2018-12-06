# -*- coding: utf-8 -*-

s1 = set([1, 1, 2, 2, 3, 3])
print(s1)
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

'''
print:
{1, 2, 3}
{2, 3}
{1, 2, 3, 4}
'''


s1.add(5)
print(s1) 
s2.remove(4)
print(s2)


'''
print:
{1, 2, 3, 5}
{2, 3}
'''