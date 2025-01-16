import re 

# get email 
email_address = input("Enter you personal email address '(you@(domain).com)': ")
# gabrielasar5434@outlook.com
email_patterns = ("^[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z0-9]")
if re.match(email_patterns,email_address):
    print('Valid Email')

else: 
    print('Invalid Email')

