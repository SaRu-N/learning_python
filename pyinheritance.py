class Polygon:
    def __init__(self,sides):
        self.n=sides
        self.sides=[0 for i in range(sides)]
    def inputSides(self):
        self.sides=[float(input("Enter side"+str(i+1)+" : "))for i in range(self.n)]
    def display(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])


class Rectangle(Polygon):
    def __init__(self):
        super().__init__(2)
        # Polygon.__init__(self,2)
    def Area(self):
        l,b=self.sides
        area=l*b
        print(f"Area={area}")

r=Rectangle()

r.inputSides()
r.display()
r.Area()
