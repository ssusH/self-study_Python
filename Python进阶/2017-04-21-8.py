# -*- coding: utf-8 -*-
#请编写一个函数calc_prod(lst)，它接收一个list，返回一个函数，返回函数可以计算参数的乘积。
#---------------------------------------------------
def prod(x,y):
    return x*y

def calc_prod(lst):
    def i():
        return reduce(prod,lst)
    return i

f = calc_prod([1, 2, 3, 4])
print f()
