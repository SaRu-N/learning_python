class Human:
    classes="Vertibates"

    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sing(self,song):
        return f"{self.name} sings {song} "

harry =Human("harry",45)
sam =Human("sam",78)


print("harry is a {}".format(harry.__class__.classes))
print(f"sam is a {sam.__class__.classes}")


print(f"{harry.name} is {harry.age} years old")
print(f"{sam.name} is {sam.age} years old")

print(harry.sing("Hello"))