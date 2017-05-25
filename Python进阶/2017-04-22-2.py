## -*- coding: UTF-8 -*-
##请思考带参数的@decorator，@functools.wraps应该放置在哪：
##
##def performance(unit):
##    def perf_decorator(f):
##        def wrapper(*args, **kw):
##            ???
##        return wrapper
##    return perf_decorator
##---------------------------

import time,functools

def performance(unit):
    def a(f) :
        @functools.wraps(f)
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

print factorial.__name__
