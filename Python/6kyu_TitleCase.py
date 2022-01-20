#A string is considered to be in title case if each word in the string is either (a) capitalised 
#(that is, only the first letter of the word is in upper case) or (b) considered to be an 
#exception and put entirely into lower case unless it is the first word, which is always capitalised.

#Write a function that will convert a string into title case,
#given an optional list of exceptions (minor words). 
#The list of minor words will be given as a string with each word separated by a space. 
#Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of 
# he minor word string is changed.


def title_case(title, minor_words = ''):
    if title == '':
        return ''
    title = title.lower()
    title = title.split()
    
    if minor_words != '':
        minor_words = minor_words.lower()
        minor_words = minor_words.split()
    result = []
    listToStr = ''


    for word in title:
    
        if word not in minor_words:
            result.append(word.capitalize())

        else:
            result.append(word)

    first_letter = result[0].capitalize()
    result.remove(result[0])
    result.insert(0, first_letter)

    listToStr = ' '.join(map(str, result)) # convert list to string
    
    return listToStr

