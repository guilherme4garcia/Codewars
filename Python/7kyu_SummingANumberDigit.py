#Write a function named sumDigits which takes a number as input
#and returns the sum of the absolute value of each of the number's decimal digits.


def sum_digits(number):
    
    if number < 0:
        number = number * (-1)

    s = str(number)
    sum = 0
    
    for dig in s:
        sum += int(dig)
    
    return sum