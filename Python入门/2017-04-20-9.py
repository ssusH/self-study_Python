# -*- coding: utf-8 -*-
#一元二次方程的定义是：ax² + bx + c = 0

#请编写一个函数，返回一元二次方程的两个解。

#注意：Python的math包提供了sqrt()函数用于计算平方根。
#-------------------------------------------------
import math

def quadratic_equation(a, b, c):
    return (-b+math.sqrt (b*b-4*a*c))/(2*a),(-b-math.sqrt(b*b-4*a*c))/(2*a)

print quadratic_equation(2.0, 3.0, 0)
print quadratic_equation(1.0, -6.0, 5.0)
