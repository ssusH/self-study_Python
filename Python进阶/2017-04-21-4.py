# -*- coding: utf-8 -*-
#利用add(x,y,f)函数，计算：
#---------------------------------------------------
import math

def add(x, y, f):
    return f(x) + f(y)

print add(25, 9, math.sqrt)
