# -*- coding: UTF-8 -*-
##
##上一节的@performance只能打印秒，请给 @performace 增加一个参数，允许传入's'或'ms'：
##
##@performance('ms')
##def factorial(n):
##    return reduce(lambda x,y: x*y, range(1, n+1))
##---------------------------

import time

def performance(unit):
    def a(f) :
        def b(*args,**kw):
            t1=time.time()
            c = f(*args,**kw)
            t2= time.time()
            if unit=='ms':
                t = (t2 - t1) * 1000
            else :
                t=(t2 - t1)
            print 'call %s() in %f %s'%(f.__name__, t, unit)
            return c
        return b 
    return a

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print factorial(10)
