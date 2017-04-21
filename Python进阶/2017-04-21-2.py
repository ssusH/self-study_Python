# -*- coding: utf-8 -*-
#请编写一个函数，它接受一个 list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略。
#---------------------------------------------------
def toUppers(L):
    return [x.upper() for x in L if isinstance(x,str)]

print toUppers(['Hello', 'world', 101])
