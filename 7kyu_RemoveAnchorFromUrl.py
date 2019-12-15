url = 'www.codewars.com'


anchor = url.find('#')

if anchor == -1:
    print(url)
else:
    print(url[:anchor])

print(anchor)