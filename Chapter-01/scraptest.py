from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.h1)
# This returns only the h1 tag of the page
# When you call 

## Connecting Reliably and Handling Exceptions
# Let us look at the first line of our scraper, after the imprt statements
# and figure out how to handle any exceptions this might throw
html = urlopen('http://pythonscraping.com/pages/page1.html')

# Tow main things can happen: page not found on server, the server was not found
# You can handle this errors in this way:
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
try:
    html = urlopen('http://pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
    # This will print the error code and the error message
except URLError as e:
    print('The server could not be found!')
else:
    print('It worked')

# If the page is retrieved successfully from he server, there is still an issue of
# the content on the page not quite being what you expected. Everytime you access a 
# tag in a BeautifulSoup object, it's smart to add a check to make sure the tag 
# actually exiists. If you attempt to access a tag that does not exist, Beautifulsoup
# will return a None object. The problem is, attempting to access a tag on a None 
# object will result in an AttributeError being thrown
# The following line will return a None object:
print(bs.NoneExistentTag.someTag)

# The best way is to check for both instances
try:
    badContent = bs.NonExistentTag.anotherTag
except AttributeError as e:
    print('Tag was not found')
else:
    if badContent == None:
        print('Tag was not found')
    else:
        print(badContent)


# This code can be written in a different way:
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found')
else:
    print(title)
