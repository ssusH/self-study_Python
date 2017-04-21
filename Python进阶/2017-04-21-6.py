# -*- coding: utf-8 -*-
#请利用filter()过滤出1~100中平方根是整数的数，即结果应该是：

#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#---------------------------------------------------
import math

def is_sqr(x):
    a,b = math.modf(math.sqrt(x))
    return a==0

print filter(is_sqr, range(1, 101))

a ='\t\t123\r\n'
print a.strip()
# s.strip(rm) 删除 s 字符串中开头、结尾处的 rm 序列的字符。

#当rm为空时，默认删除空白符（包括'\n', '\r', '\t', ' ')

