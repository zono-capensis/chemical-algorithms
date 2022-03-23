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
#print(poly)

interval = poly.find_root_interval()
#print(interval)

derivative = functions.find_derivative(poly)
#print(derivative)

p2 = functions.synth_division(poly.list_of_coefficients, derivative.list_of_coefficients)
#print(p2)

dividend = poly
divisor = derivative
sturm_sequence = [poly,derivative]
is_not_finished = True
actual_degree = derivative.degree -1
while is_not_finished:
    remainder = functions.synth_division(dividend.list_of_coefficients, divisor.list_of_coefficients)
    temp_poly = Polynomial(degree=actual_degree,list_of_coefficients=remainder)
    print(temp_poly)
    actual_degree-=1
    sturm_sequence.append(temp_poly)
    dividend = divisor
    divisor = temp_poly
    if len(remainder)<1:
        is_not_finished = False

for i in sturm_sequence:
    print(i)





