'''
    Persistent Bugger. 

    Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
    which is the number of times you must multiply the digits in num until you reach a single digit.'''

def persistence(n):
    n = str(n)
    contador = 0
    while len(n) > 1:
        multi = 1
        for digit in n:
            multi *= int(digit)
        n = str(multi)
        contador += 1        
    
    return contador