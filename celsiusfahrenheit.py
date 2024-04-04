"""Temperaturen umwandeln.


..Python Library

"""

def fahrenheit_to_celsius(fahrenheit):
    # convert fahrenheit to celsius
    tempc = (fahrenheit-32)/1.8
    return tempc

def celsius_to_kelvin(celsius):
    # convert celsius to kelvin
    tempk = celsius + 273.15
    return tempk

def fahrenheit_to_kelvin(fahrenheit):
    # convert fahrenheit to kelvin
    w = celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))
    return w

fahrenheit = 90 #float(input("Temperatur in Fahrenheit: ")) #Eingabeaufforderung
celsius = round(fahrenheit_to_celsius(fahrenheit),2)
kelvin = round(fahrenheit_to_kelvin(fahrenheit),2)
print("Fahrenheit:", fahrenheit)
print("Celsius:", celsius)
print("Kelvin:",  kelvin)

