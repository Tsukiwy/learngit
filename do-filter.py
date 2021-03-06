# -*- coding: utf-8 -*-
'''
回数是指从左向右读和从右向左读都是一样的数，例如12321，909。
请利用filter()筛选出回数
'''
#方案一:
def is_palindrome(n):
    nn = str(n) #转成字符串
    return nn == nn[::-1] #反转字符串并对比原字符串返回true/false
    
    
#方案二：
def is_palindrome(n):
      s = str(n)
      h = list(range((len(s))//2))
      for i in h:
          if s[i] != s[-(i+1)]:
             return False
      return True

#方案三:
print (list(filter(lambda n : str(n)==str(n)[::-1],range(1,1000))))

 
# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

