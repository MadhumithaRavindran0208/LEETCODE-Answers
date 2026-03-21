class Solution(object):
    def convertTemperature(self, celsius):
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
        return (list([kelvin,fahrenheit]))