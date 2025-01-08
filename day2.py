# a program that takes user name and age and displays a greeting message together with their age 

# there is a cleaner way but i chose this 

import datetime # a library to work with date and time

current_year = datetime.datetime.now().year # get the current year automatically

name = input('Enter your name: ').title().strip()# start name with uppercase and get rid of whitespaces
age = int(input('Enter your age: '))
results = current_year - age 

print(f'Hello! {name}, you were born in the year {results}')

        
        
        
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        