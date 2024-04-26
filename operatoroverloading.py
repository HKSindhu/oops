class ComplexNumber:
    def __init__(self,real,imaginary):
        self.real=real
        self.imaginary=imaginary
    def __add__(self,other):
        return (f"{self.real+other.real}+{self.imaginary+self.imaginary}i")
c1=ComplexNumber(2,2)
c2=ComplexNumber(1,2)
print(c1+c2)

class Party:
    def __init__(self,name,money):
        self.name=name
        self.money=money
    def __gt__(self,other):
        if self.money>other.money:
            return True
        else:
            return False
p1=Party("sindhu",1000)
p2=Party("kunni",2000)
if p1>p2:
    print(f"{p1.name} will pay the bill")
else:
    print(f"{p2.name} will pay the bill")