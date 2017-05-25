## -*- coding: UTF-8 -*-
##在Python 3.x中，字符串统一为unicode，不需要加前缀 u，而以字节存储的str则必须加前缀 b。请利用__future__的unicode_literals在Python 2.7中编写unicode字符串。
##---------------------------

from __future__ import unicode_literals

s = 'am I an unicode?'
print isinstance(s, unicode)
