# num1=float(input("Enter First Number:"))
# num2=float(input("Enter Second Number:"))
# # we can make num1 as number in here too int(num1) or float(num1)
# result=num1+num2
# print("sum is "+str(result))
# result1=num1-num2
# print("Difference is "+str(result1))
# result2=num1*num2
# print("Product is "+str(result2))
# result3=num1/num2
# print("Division: "+str(result3))
# result4=num1%num2
# print("Remainder: "+str(result4))

num1=float(input("Enter First Number:"))
op=input("Enter operator:")
num2=float(input("Enter second Number:"))
# num3=float(input("Enter Third Number:"))
if op== "+":
    print("sum is "+str(num1+num2))
elif op=="-":
    print("difference is "+str(num1-num2))
elif op=="*":
    print("product is "+str(num1*num2))
elif op=="/":
    print("remainder is "+str(num1/num2))
else:
    print("enter valid operator(+,-,*,/")