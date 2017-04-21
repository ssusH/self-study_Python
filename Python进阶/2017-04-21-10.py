# -*- coding: utf-8 -*-
#返回闭包不能引用循环变量，请改写count()函数，
#让它正确返回能计算1x1、2x2、3x3的函数。
#-----------------------------------
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j*j
            return g
        r = f(i)
        fs.append(r)
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()

# '错误的案例'
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1, f2, f3 = count()
print f1(), f2(), f3()
