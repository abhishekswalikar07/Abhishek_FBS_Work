# Create a class Complex Number with data members as real and imag and add
# following methods :
# a. Constructor
# b. Destructor
# c. Overload +,- operator

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        print("Constructor called...")

    def __add__(self, other):
        r = self.real + other.real
        i = self.imag + other.imag
        if i>=0:
            sign="+"
        else:
            sign="-"
        return f"{r} {sign} {abs(i)}i"

    def __sub__(self, other):
        r = self.real - other.real
        i = self.imag - other.imag
        
        if i>=0:
            sign="+"
        else:
            sign="-"

        return f"{r} {sign} {abs(i)}i"
    
    def __del__(self):
        print("Destructor called!!!")

c1 = ComplexNumber(3, 6)
c2 = ComplexNumber(1, 5)

print("Addition of complext numbers:",c1 + c2)   
print("Subtraction of complex numbers:",c1 - c2)   