# -*- coding: utf-8 -*-
#在生成的表格中，对于没有及格的同学，请把分数标记为红色。

#提示：红色可以用 <td style="color:red"> 实现。
#---------------------------------------------------
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def generate_tr(name, score):
    if score<60 :
        return '<tr><td>%s</td><td style="color:red">%s</td></tr>' % (name, score)
    return '<tr><td>%s</td><td>%s</td></tr>' % (name, score)

tds = ['<tr><td>%s</td><td>%s</td></tr>'%(name,score) for name, score in d.iteritems()]
print '<table border="1">'
print '<tr><th>Name</th><th>Score</th><tr>'
for name,score in d.iteritems():
    print '\n',generate_tr(name, score)
print '</table>'
