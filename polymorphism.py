class Cat:
    def eat(self):
        print("Cat can eat")
    def run(self):
        print("Cat can run")
class Fish:
    def eat(self):
        print("Fish can't eat")
    def swim(self):
        print("Fish can swim")

def eating_cap(animal):
    animal.eat()

kitty =Cat()
Hat=Fish()

eating_cap(kitty)
eating_cap(Hat)

