# -*- coding: utf-8 -*-
#给定一个dict：

#d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

#请计算所有同学的平均分。
#-------------------------------------------------
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum = 0.0
for i in d.values():
    sum+=i;
print sum/len(d.values())
