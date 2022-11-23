def printer():
    print("hello world")
def display_info(func):
    def inner():
        print("Executing",func.__name__,"function")
        func()
        print("Done Executing")
    return inner
decorated_func=display_info(printer)
decorated_func()


print("using @ symbol")
def display_info(func):
    def inner():
        print("Executing",func.__name__,"function")
        func()
        print("Done Executing")
    return inner
@display_info
def printer():
    print("hello world")
printer()

print("Decorators with parameter")
def smart_divide(func):
    def inner(a,b):
        print("Dividing",a,"by",b)
        if b==0:
            print("b must not be 0")
            return
        return func(a,b)
    return inner
@smart_divide
def divide(a,b):
    return a/b
value1=divide(25,5)
print(value1)
value2=divide(5,0)
print(value2)

print("Changing decorators")

def star(func):
    def inner(arg):
        print("*"*30)
        func(arg)
        print("*"*30)
    return inner
def hash(func):
    def inner(arg):
        print("#"*30)
        func(arg)
        print("#"*30)
    return inner

@star
@hash

def output(msg):
    print(msg)
output("Decorators are awesome")


