class Polynomial:

    def __init__(self,degree=0,list_of_coefficients=[]):
        self.degree = degree
        self.list_of_coefficients = list_of_coefficients

    def find_root_interval(self):
        numerator=0
        for addend in self.list_of_coefficients[1::]:
            numerator+= abs(addend)
        temp_sup = numerator / (abs(self.list_of_coefficients[0]))
        temp_inf = temp_sup * (-1)
        sup = max(temp_sup,1)
        inf = min(temp_inf, 1)
        return (inf,sup)

    def __str__(self):
        polynomial=""
        for i in range(len(self.list_of_coefficients)):
            coefficient = self.list_of_coefficients[i]
            if (coefficient!=0):
                variable = "x^"+str(self.degree-i)
                sign = ""

                if (coefficient>0):
                    sign = "+"
                    if i==0:
                        sign=""

                coefficient = "" if coefficient==1 else str(coefficient)
                
                if (self.degree-i==1):
                    variable = "x"
                if (self.degree-i==0):
                    variable= ""

                polynomial += sign + coefficient + variable

        return polynomial
