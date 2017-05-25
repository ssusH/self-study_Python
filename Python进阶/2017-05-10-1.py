class Person(object):
    def __init__(self, name, score):
        self.name = name
        self._score = score

p = Person('Bob', 59)

print p.name
print p.__score
