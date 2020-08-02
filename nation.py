#! /usr/bin/env python

d_persons= {'Guillaume':'Canada', 'Niklas':'Germany', 'Mark':'USA', 'Alex':'Swiss', 'Alberto':'Italia'}


class Person():
    nation = 'A nation'
    name = 'username'

    def setName(self,target):
        self.name = target

    def findNation(self,d_persons):
        self.nation = d_persons[self.name]
            
    def showName(self):
        print(d_persons[self.name])
           
    def showNation(self):
        print(self.nation)

yune = Person()
yune.setName('Mark')
yune.showNation(d_persons.keys[0])

#print(p1.assignNation())
#print(p1.showName())
#print(p1.showNation())

#print(p1.findNation())
#print(p1.findNation('Mark'))
