# -*- coding: utf-8 -*-
#请定义一个 greet() 函数，
#它包含一个默认参数，
#如果没有传入，打印 'Hello, world.'，
#如果传入，打印 'Hello, xxx.'
#-------------------------------------------------
def greet(a='world'):
    print 'Hello,',a,'.'

greet()
greet('Bart')
