def camel_case(string):
    quote = string.split(' ')
    capitalizada = ''
    
    for word in quote:
        capitalizada += word.capitalize()
    
    return capitalizada