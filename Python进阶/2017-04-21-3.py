# -*- coding: utf-8 -*-
#请编写一个函数，它接受一个 list，然后把list中的所有字符串变成大写后返回，非字符串元素将被忽略。
#---------------------------------------------------
print [x*100+y*10+z for x in range(1,10) for y in range(0,10) for z in range(0,10) if x == z]
