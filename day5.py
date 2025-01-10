# factorial of a number 
def number(n):
    if n == 0:
        return 1 
    else: 
        return n * number(n-1)
    
results = number(6) # put in a number 
print(results)


