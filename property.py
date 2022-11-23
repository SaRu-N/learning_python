class Celsius:
    def __init__(self, temperature=0):
        self.set_temperature(temperature)
    def to_fahrenheit(self):
        return (self.get_temperature()*1.8)+32
    
    #getter method
    def get_temperature(self):
        return self._temperature
    #setter method
    def set_temperature(self,value):
        if value <-273.15:
            raise ValueError("temperature below -273.15")
        self._temperature =value
# Create a new object, set_temperature() internally called by __init__
human =Celsius(37)

# Get the temperature attribute via a getter
print(human.get_temperature())
# Get the to_fahrenheit method, get_temperature() called by the method itself
print(human.to_fahrenheit())
# new constraint implementation
# human.set_temperature(-300)
# Get the to_fahreheit method
# print(human.to_fahrenheit)

print("using property class")
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)
human=Celsius(37)
print(human.get_temperature())
print(human.to_fahrenheit())


# print(human.temperature)
# human.temperature=89

print("Using @property decorator")
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value


# create an object
human = Celsius(37)

print(human.temperature)

print(human.to_fahrenheit())

coldest_thing = Celsius(-300)