# Write a function that accepts an array of 10 integers (between 0 and 9),
# that returns a string of those numbers in the form of a phone number.

# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parentheses!

def create_phone_number(n):

    ddd = ''
    tel1 = ''
    tel2 = ''

    for number in range(len(n)):
        if number < 3:
            ddd += str(n[number])
        if 2 < number < 6:
            tel1 += str(n[number])
        if 5 < number < 10:
            tel2 += str(n[number])

    return f'({ddd}) {tel1}-{tel2}'