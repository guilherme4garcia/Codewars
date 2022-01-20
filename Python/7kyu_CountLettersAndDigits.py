'''
    Bob is a lazy man.
    He needs you to create a method that can determine how many letters and digits are in a given string.
    example:
    "hel2!lo" --> 6
    "wicked .. !" --> 6
    "!?..A" --> 1
    '''

def count_letters_and_digits(s):
    contador = 0
    if s == None:
        return 0
    else:
        for x in s:
            if x.isalnum() == True:
                contador += 1
        return contador