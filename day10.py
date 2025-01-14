from math import sqrt

# square root of a number 
try:
    enter_number = int(input('Enter a number to find its square root: '))
    print(f'The square root of {enter_number} is {sqrt(enter_number)}')

except ValueError:
    print('Invalid Input!')