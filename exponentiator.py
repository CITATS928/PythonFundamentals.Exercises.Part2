#Exercise3
def exponentiate(num1,num2):
    """
    This function is to raise the num1 to the num2 power
    """
    return num1 ** num2

"""power of 4"""
def raise_to_fourth_power(num):
    return exponentiate(num,4)

square = lambda x : x**2 #power of 2
cube = lambda x:x**3     #power of 3

print(square(2))
print(cube(2))
print(raise_to_fourth_power(2))