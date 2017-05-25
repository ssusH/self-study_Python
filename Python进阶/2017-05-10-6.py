class Person(object):

    __count = 0

    def __init__(self,name):
        self.name = name
        Person.__count+=1
        
    @classmethod
    def how_many(cls):
        return cls.__count
        
    @classmethod
    def pr(cls):
        print 'prprpr'
        

print Person.how_many()

p1 = Person('Bob')

print Person.how_many()
Person.pr()
