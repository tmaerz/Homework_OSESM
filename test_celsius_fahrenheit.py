from celsiusfahrenheit import fahrenheit_to_celsius
from celsiusfahrenheit import fahrenheit_to_kelvin
from celsiusfahrenheit import celsius_to_kelvin


def test_fahrenheit_to_celsius():
    assert round(fahrenheit_to_celsius(90), 2) == 32.22
    assert round(fahrenheit_to_kelvin(90), 2) == 305.37
    assert round(celsius_to_kelvin(20), 2) == 293.15


