# The goal is to link two unlikely subjects (in the first case, Wikipedia articles that link
# to each other, and in the second case, actors appearing in the same film) by a chain
# containing no more than 6 total(including two original subjects)
# In this section, you'll begin a project that will become Six Degress of Wikipedia
# solution finder : You'll be able to take the Eric Idle page and find the fewest number of link 
# clicks that will take you to the Kevin Bacon page

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
bs = BeautifulSoup(html, 'html.parser')
for link in bs.find_all('a')