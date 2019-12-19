#You are going to be given a word. Your job is to return the middle character of the word. 
#If the word's length is odd, return the middle character.
#If the word's length is even, return the middle 2 characters.

def get_middle(s):
    if len(s) % 2 != 0:
        middle = s[len(s)//2]
    else:
        middle = s[len(s)//2 - 1:len(s)//2 + 1]

    return middle