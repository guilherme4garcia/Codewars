#Check to see if a string has the same amount of 'x's and 'o's. 
#The method must return a boolean and be case insensitive. 
#The string can contain any char.

def xo(s):
    s = s.lower()
    contador_x = s.count('x')
    contador_o = s.count('o')

    if contador_x == contador_o:
        return True
    else:
        return False