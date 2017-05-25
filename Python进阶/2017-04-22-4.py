## -*- coding: UTF-8 -*-
##Python的os.path模块提供了 isdir() 和 isfile()函数，请导入该模块，并调用函数判断指定的目录和文件是否存在。
##
##注意: 
##
##1. 由于运行环境是平台服务器，所以测试的也是服务器中的文件夹和文件，该服务器上有/data/webroot/resource/python文件夹和/data/webroot/resource/python/test.txt文件，大家可以测试下。
##
##2. 当然，大家可以在本机上测试是否存在相应的文件夹和文件。
##
##import os
##print os.path.isdir(r'C:\Windows')
##print os.path.isfile(r'C:\Windows\notepad.exe')
##---------------------------

import os.path

print os.path.isdir(r'C:\Windows')
print os.path.isfile(r'C:\Windows\notepad.exe')
