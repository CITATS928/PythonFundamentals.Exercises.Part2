#Exercise3
def exponentiate(num1,num2):
    return num1 ** num2

def raise_to_fourth_power(num):
    return exponentiate(num,4)

square = lambda x : x**2
cube = lambda x:x**3

print(square(2))
print(cube(2))
print(raise_to_fourth_power(2))