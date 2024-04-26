#method overloading1
class Demo:
    def add(self,a,b,c=0):
        return a+b+c
    
d=Demo()
print(d.add(2,3))
print(d.add(10,20,30))


#2
class Demo:
    def add(self,*args):
        total=0
        for i in args:
            total=total+i
        return total
    
d=Demo()
print(d.add(2,3))
print(d.add(10,20,30))
