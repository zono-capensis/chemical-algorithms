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

dividend= Polynomial(degree, list_of_coefficients)
divisor = functions.find_derivative(dividend)

coefficients_of_remainder = functions.synth_division(dividend.list_of_coefficients, divisor.list_of_coefficients)
current_degree = divisor.degree - 1
remainder = Polynomial(current_degree,coefficients_of_remainder)

sturm_sequence = [dividend,divisor,remainder]

while current_degree > 0:
    dividend = divisor
    divisor = remainder
    
    coefficients_of_remainder = functions.synth_division(dividend.list_of_coefficients, divisor.list_of_coefficients)
    current_degree = divisor.degree - 1
    remainder = Polynomial(current_degree,coefficients_of_remainder)
    sturm_sequence.append(remainder)

for poly in sturm_sequence:
    print(poly)
