# a program that catches an error if the user inputs a non-integer

try:
    enter_number = int(input('Enter a number: '))
    print(enter_number)

except ValueError:
    print('Invalid Input')