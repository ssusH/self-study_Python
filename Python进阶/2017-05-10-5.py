import types

def paintname(self):
    print self.name

class Person(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'

p1 = Person('Bob', 90)
p1.getname = types.MethodType(paintname,p1,Person)
print p1.get_grade
print p1.get_grade()
p1.getname()
