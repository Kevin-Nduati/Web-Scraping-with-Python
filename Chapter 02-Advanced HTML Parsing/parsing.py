# Keep in mind that layering the techniques in this section with 
# reckless abandonment can lead to code which is difficult to debug,
# fragile or both

# Let us say you have some atrget content. Maybe it's buried 20
# tags deep in an HTML mush with no helpful tags or HTML attributes
# to be found. So you end up writing something like this:
bs.find_all('table')[4].find_all('tr')[2].find('td').find_all('div').\
    find_all('div')[1].find_all('a')

# This doesn't look so great. In addition to the aesthetics of the line,
# even the slightest change to the website by a site administrator might
#  break your web scraper altogether. So ypur options are
# 1. Look for a print this pahe link -present yourself as a mobile
# 2. Look for the info hidden in javascript file
# 3. Info might be available in the URL of the age itself


# Let us create a webscraper for:http://
# www.pythonscraping.com/pages/warandpeace.html
# On this page, the lines spoken by characters are in red, whereas
# the names of characters are in green. There are span tags that 
# reference the appropriate CSS classes

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html, 'html.parser')

# Using this BeautifulSoup object, you can use the 'find_all' function
# to extract a Python list of proper nouns found by selecting only
# the text  within the span green tags

nameList = bs.find_all('span', {'class': 'green'})
for name in nameList:
    print(name.get_text())

# When run, it lists all the proper nouns in the text, in the order 
# they appear in war and peace 
print(nameList)

# find() and find_all() are the two functions you will likely use 
# the  most. The find() function returns the first tag found, while
# the find_all() function returns a list of all tags found. The 
# arguments to find_all() are the tag name and a dictionary of
# attributes. The dictionary is used to specify the attributes of
# the tag you are looking for. 

# find_all(tag, attributes, recursive, text, limit, keywords)
# find(tag, attributes, recursive, text, keywords)


# The attributes argument takes a dictionary of key-value pairs.
# For example to find both green and red span tags in the html document:
find_all('span', {'class':{'green', 'red'}})

# The recursive argument is bolean. How deep do you want to go?
# If recursive is set into True, the find_all function will search
# the entire tree of the tag. If it is set to False, it will only
# search the immediate children of the tag.

# The text argument is a string. If you want to find a tag with
# a particular text, you can use the text argument. Forexample, if
# you  want to find the number of times 'the prince' is surrounded
# by tags on the example page, you could replace your .find_all()
# function in the previous example with the following lines:

nameList = bs.find_all(text='the prince')
print(len(nameList))

# The keyword argument allows you to select tags that contain a 
# particular attribute or set of attributes
title = bs.find_all(id='title', class_='text')
# This returns the 1st tag with the word 'text' in the class attribute
# and the id attribute of 'title'

