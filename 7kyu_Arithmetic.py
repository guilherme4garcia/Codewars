#Make a function that does arithmetic!

#Given two numbers and an arithmetic operator (the name of it, as a string), return the result of the two numbers having that operator used on them.

#a and b will both be positive integers, and a will always be the first number in the operation, and b always the second.

#The four operators are "add", "subtract", "divide", "multiply".


def arithmetic(a, b, operator):
    
    result = 0
    if operator == "add":
        result = a + b
    if operator == "subtract":
        result = a - b
    if operator == "multiply":
        result = a * b
    if operator == "divide":
        result = a / b
    
    return result