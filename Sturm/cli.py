

def get_coefficients():
    return [coefficient for coefficient in input("Please type the coefficients: ").split(",")]

def get_degree():
    return input("Type the degree of the polynomial: ")

def welcome():
    print("***********************************************************")
    print("This program compute the real roots of a given polynomial. ")
    print("It needs the degree of the polynomial")
    print("And all the coefficients of the polynomial")
    print("Please note that the fist coefficient must not be zero and")
    print("if a monomial does not appear, its coefficient is zero.")
    print("Provide the coefficients (including 0) separated by commas.")
    print("***********************************************************")
