# -*- coding: utf-8 -*-
#请编写接受可变参数的 average() 函数。
#-------------------------------------------------
def average(*args):
    i = 0.0
    _sum = 0.0
    for a in args:
        _sum+=a
        i+=1
    if i == 0:
        return i
    else:
        return _sum/i

print average()
print average(1, 2)
print average(1, 2, 2, 3, 4)
