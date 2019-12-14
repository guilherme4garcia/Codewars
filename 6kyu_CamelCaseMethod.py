#Write simple .camelCase method for strings.
#All words must have their first letter capitalized without spaces.

#For instance:
#camelcase("hello case") => HelloCase
#camelcase("camel case word") => CamelCaseWord


def camel_case(string):
    quote = string.split(' ')
    capitalizada = ''
    
    for word in quote:
        capitalizada += word.capitalize()
    
    return capitalizada