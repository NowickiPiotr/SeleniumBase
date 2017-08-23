# https://www.programiz.com/python-programming/property

class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

sd = Celsius(35)
sd.temperature = -23
print(sd.temperature)


if sd.temperature is not None:
    print("dsa")