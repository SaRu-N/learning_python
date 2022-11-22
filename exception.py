try:
    numerator=int(input("Enter numerator:"))
    denominator=int(input("Enter denominator:"))

    result= numerator/denominator
    print("Result=",result)

    new_list=[1,2,3]
    i=int(input("Input index:"))
    print(new_list[i])
except ZeroDivisionError:
    print("Denominator cannot be 0. Please Try again")
except IndexError:
    print("Index cannot be Greater than size of list")
finally:
    print("this runs whatever the situation is.")