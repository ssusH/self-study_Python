# -*- coding: utf-8 -*-
#################################################
##请创建包含两个 Person 类的实例的 list，
##并给两个实例的 name 赋值，
##然后按照 name 进行排序。
#################################################
def cmp_ignore_case(s1, s2):
    if s1.name[:1].upper() > s2.name[:1].upper():
        return 1
    elif s1.name[:1].upper() < s2.name[:1].upper():
        return -1
    else:
        return 0


class Person(object):
    pass

p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
L2 = sorted(L1,cmp_ignore_case)

for i in L2:
    print i.name

print L2[0].name
print L2[1].name
print L2[2].name
