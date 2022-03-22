#!/usr/bin/python

import cli
import functions
from utils import  Polynomial

cli.welcome()
degree = cli.get_degree()
degree = functions.string_to_int(degree)
while not (float('inf')!=degree): degree = functions.string_to_int(degree)

list_of_coefficients = cli.get_coefficients()
for i in range(len(list_of_coefficients)):
    list_of_coefficients[i]=functions.string_to_int(list_of_coefficients[i])

poly = Polynomial(degree, list_of_coefficients)
print(poly)

interval = poly.find_root_interval()
print(interval)

derivative = functions.find_derivative(poly)
print(derivative)







