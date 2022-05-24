
is_male =True
is_tall =False
# if is_male:
#     print("You are a male")
# else:
#     print("May be you are Female")
# 
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif is_tall and not(is_male):
    print("You are tall but not man")
else:
    print("May be you are Female or not tall")

def max_num(num1,num2,num3):
    if(num1>=num2 and num1>=num3):
        print(str(num1)+" is greater")
    elif(num2>=num1 and num2>=num3):
        print(str(num2)+" is greater")
    else:
        print(str(num3)+" is greater")
max_num(7,9,2)
