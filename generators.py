def even_generator():
    n=0
    n+=2
    yield n
    n+=2
    yield n
    n+=2
    yield n
    
    pass
numbers=even_generator()
print(next(numbers))
print(next(numbers))
print(next(numbers))

print("using loop")
def even_generator(max):
    n=2

    while n<=max:
        yield n
        n+=2
for i in even_generator(10):
    print(i)

print("Using custom Generator")
def generate_fibo(max):
    n1=0
    n2=1
    while(n1<max):
        yield n1
        n1,n2 =n2, n1+n2
    
for i in generate_fibo(40):
    print(i)