class Complex:
    def __init__ (self,r=0,i=0):
        self.real=r
        self.imag=i
    def getData(self):
        print(f"{self.real}+{self.imag}i")

num1=Complex(2,3)

num1.getData()

num2=Complex(5)
num2.attr =10
num2.imag=1

print((num2.real, num2.imag, num2.attr))

# print(num1.attr)
print((num1.real, num1.imag))

del num1.imag
print((num1.real, num1.imag))
