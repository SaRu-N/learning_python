def add(num1, num2):
    def output():
        num3 =num1+num2
        print("Sum:",num3)
    return output
next=add(10,20)
next()

def find_sum(num1):
    def sum(num2):
        return num1+num2
    return sum

sum1=find_sum(10)
sum2=find_sum(20)

print(sum1(10))
print(sum2(20))

find_sum.__closure__
print(sum2.__closure__)
print(sum2.__closure__[0].cell_contents)