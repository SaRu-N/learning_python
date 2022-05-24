# for letter in "Learning Python":
#     print(letter)
# days =["Sunday", "Monday","Tuesday"]
# for day in days:
#     print(day)
# for index in range(2):
#     print(index)
# for item in range(2,5):
#     print(item)
# for index in range(len(days)):
#     print(days[index])
# for index in range(5):
#     if index==0:
#         print("First")
#     else:
#         print("not first")

def raise_to_power(base_num,power_num):
    result=1
    for index in range(power_num):
        result=base_num*base_num
    return result
print("The result is "+str(raise_to_power(8,8)))