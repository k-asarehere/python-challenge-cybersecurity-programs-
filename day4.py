
def count(n):
    print(n)
    while n:                                                                                            
        n -= 1 
        if n == 0:
            return 1 
        else:
            print(n)


count(10)