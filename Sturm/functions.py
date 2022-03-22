from utils import Polynomial

def string_to_int(number):
    try:
        number= int(number)
    except ValueError:
        number = float('inf')
    return number

def string_to_float(number):
    try:
        number= float(number)
    except ValueError:
        number = float('inf')
    return number

def find_derivative(polynomial):
    list_of_deri_coefficients = []
    degree_iterator = polynomial.degree

    for i in range(polynomial.degree):
        list_of_deri_coefficients.append(polynomial.list_of_coefficients[polynomial.degree - degree_iterator]*(degree_iterator))
        degree_iterator-=1

    return Polynomial(polynomial.degree-1, list_of_deri_coefficients)

def remainder_of_polinomials(poly_a,poly_b):
    
        
    
