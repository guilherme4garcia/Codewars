#Complete the function/method so that it returns the url with anything after the anchor (#) removed.

def remove_url_anchor(url):
    
    anchor = url.find('#')   #searching the position of the parameter

    if anchor == -1:         #-1 == not found
        return url
    else:
       return url[:anchor]   