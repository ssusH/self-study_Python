## -*- coding: UTF-8 -*-
##在第7节中，我们在sorted这个高阶函数中传入自定义排序函数就可以实现忽略大小写排序。请用functools.partial把这个复杂调用变成一个简单的函数：
##
##sorted_ignore_case(iterable)
##---------------------------

import functools

def a(x,y):
    if x.upper()>y.upper():
        return 1
    elif x.upper() < y.upper():
        return -1
    else :
        return 0

sorted_ignore_case = functools.partial(sorted,cmp=a)

print sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit'])
