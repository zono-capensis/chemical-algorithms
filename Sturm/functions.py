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

def synth_division(dividend, divisor):
    #By Wikipedia
    """Fast polynomial division by using Expanded Synthetic Division. 
    Dividend and divisor are both polynomials, which are here simply lists of coefficients. 
    E.g.: x**2 + 3*x + 5 will be represented as [1, 3, 5]
    """
    out = list(dividend)  # Copy the dividend
    normalizer = divisor[0]
    for i in range(len(dividend) - len(divisor) + 1):
        # For general polynomial division (when polynomials are non-monic),
        # we need to normalize by dividing the coefficient with the divisor's first coefficient
        out[i] /= normalizer

        coef = out[i]
        if coef != 0:  # Useless to multiply if coef is 0
            # In synthetic division, we always skip the first coefficient of the divisor,
            # because it is only used to normalize the dividend coefficients
            for j in range(1, len(divisor)):
                out[i + j] += -divisor[j] * coef

    # The resulting out contains both the quotient and the remainder,
    # the remainder being the size of the divisor (the remainder
    # has necessarily the same degree as the divisor since it is
    # what we couldn't divide from the dividend), so we compute the index
    # where this separation is, and return the quotient and remainder.
    separator = 1 - len(divisor)
    #return out[:separator], out[separator:]  # Return quotient, remainder.
    return out[separator:]  # Return remainder.


