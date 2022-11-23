numbers =[2, 4,6]
# value =numbers.__iter__()
values =iter(numbers)
item1= next(values)
print(item1)
item1= next(values)
print(item1)
item1= next(values)
print(item1)
# this creates stop iteration exception
# item1= next(values)
# print(item1)

#iteration using while
print("Iteration using while")
new_list=['a','b','c']
iter_obj=iter(new_list)

while(True):
    try:
        element =next(iter_obj)
        print(element)
    except StopIteration:
        break
print("Creating Custom iterator")
class Even:
    def __init__(self, max):
        self.n = 2
        self.max=max
    def __iter__(self):
        
        return self
    def __next__(self):
       if self.n <= self.max:
            result= self.n
            self.n += 2
            return result
       else:
            raise StopIteration
numbers=Even(10)

i=iter(numbers)
print(next(numbers))
print(next(numbers))
print(next(numbers))     
print("working of self iteration using for loop")
for i in Even(10):
    print(i)