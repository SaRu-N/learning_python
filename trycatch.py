
try:
    number=int(input("Enter a number: "))
    print(number)
    value =number/0
# except ZeroDivisionError:
#  print("Divided by 0")
except ZeroDivisionError as err:
    print(err)

except ValueError:
    print("Invalid Input")
