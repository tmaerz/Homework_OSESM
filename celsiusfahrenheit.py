"""
Temperatur wird von Fahrenheit auf verschiedene Weisen in Celsius umgerechnet.
Anschließend Ausgabe als Fehrenheit, Celsius und Kelvin
"""


def fahrenheit_to_celsius(fahrenheit):
    """ convert fahrenheit to celsius"""
    tempc = (fahrenheit - 32) / 1.8
    return tempc


def celsius_to_kelvin(celsius):
    """ convert celsius to kelvin """
    tempk = celsius + 273.15
    return tempk


def fahrenheit_to_kelvin(fahrenheit):
    """ convert fahrenheit to kelvin """
    w = celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))
    return w


fahrenheit = 90  # here should be a command prompt. Pytest didn't work because of that so i changed it to a fixed value.
celsius = round(fahrenheit_to_celsius(fahrenheit), 2)  # round the result of celsius
kelvin = round(fahrenheit_to_kelvin(fahrenheit), 2)  # round the result of kelvin
print("Fahrenheit:", fahrenheit)
print("Celsius:", celsius)
print("Kelvin:", kelvin)
The test was tested in Jupyter Notebook and is running by giving the right (expected) results.
he code test (test_celsiusfahrenheit.py) depends on some packages, but the information of those is missing and shows the ModuleNotFound Error. There is no test per function, and the test didn’t fail. 

didn’t found gitignore file