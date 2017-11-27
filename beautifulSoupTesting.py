import bs4 as bs

import urllib

sauce = urllib.urlopen('https://pythonprogramming.net/parsememcparseface/').read()

soup = bs.BeautifulSoup(sauce, 'lxml')

print(soup)