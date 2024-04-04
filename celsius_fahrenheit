"""Temperaturen umwandeln.


..Python Library

"""

def fahrenheit_to_celsius(fahrenheit):
    tempc = (fahrenheit-32)/1.8
    return tempc

def celsius_to_kelvin(celsius):
    tempk = celsius + 273.15
    return tempk

def fahrenheit_to_kelvin(fahrenheit):
    w = celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))
    return w

fahrenheit = float(input("Temperatur in Fahrenheit: "))
celsius = round(fahrenheit_to_celsius(fahrenheit),2)
kelvin = round(fahrenheit_to_kelvin(fahrenheit),2)
print("Fahrenheit:", fahrenheit)
print("Celsius:", celsius)
print("Kelvin:",  kelvin)

