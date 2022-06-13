# What if you need a tag based on its location ina  document
# We will use the site http://www.pythonscraping.com/pages/page3.html
# Beautifylsoup function deals with the descendants of the current tag selected. 
# Forinstance, bs.body.h1 selects the first h1 tag in the body tag. It will
# not find tags outside the body tag.
# Similarly, bs.div.find_all('img) will find the first div tag in the document, 
# and then retrieve a list of all img tags that are descendants of that div tag.
# If you want to find only the descendants that are children, you use the
# .children tag
from cgitb import html
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

try:
    for child in bs.find('table', {'id': 'giftlift'}).children:
        print(child)
except AttributeError:
    print('An Error has occured')


## Dealing with siblings
# The beautifulsoup next_siblings() function makes it trivial to collect data 
# from table, especially one with table rows:

## let us collect tesla's stock price data from the following site
# https://www.wsj.com/market-data/quotes/TSLA/historical-prices
html = urlopen('https://www.wsj.com/market-data/quotes/TSLA/historical-prices')
bs = BeautifulSoup(html, 'html.parser')

try:
    bs.find('table', {'class': 'cr_dataTable'})
except AttributeError as e:
    print(e)
else:
    print('An error has occured')