# a program that stores user info.(name,age) in a dictionary and allows the user to retrieve it(age) by providing the name 


user_info = {}
print("*Your name and age is being stored. So,after provding it,\nre-enter(name) to retrieve your age to confirm it's stored*")
print()
name = input('Enter your name: ').title().strip() # any name
age = int(input('Enter your age: ')) # age
'''
user_info = {}
name = str 
age = int 
# To add name,age to the empty user_info dictionary,
# you have to add the name and age. So, the key will be name and value will be age # {name : age}
# this is the syntax : user_info[name] = age 
'''
user_info[name] = age 
# retrieve age 
user_name = input("Enter your name to confirm it's stored: ").title().strip()
if user_name in user_info:
    for name,age in user_info.items():
        print(f"Name: '{user_name}'\nAge: '{age}'years!")
else: 
    print('No info available!')





