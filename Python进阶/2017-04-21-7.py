# -*- coding: utf-8 -*-
#对字符串排序时，有时候忽略大小写排序更符合习惯。请利用sorted()高阶函数，实现忽略大小写排序的算法。

#输入：['bob', 'about', 'Zoo', 'Credit']
#输出：['about', 'bob', 'Credit', 'Zoo']
#---------------------------------------------------

def cmp_ignore_case(s1, s2):
    if s1[:1].upper() > s2[:1].upper():
        return 1
    elif s1[:1].upper() < s2[:1].upper():
        return -1
    else:
        return 0

print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
