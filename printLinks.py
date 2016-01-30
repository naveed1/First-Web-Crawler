import urllib
from BeautifulSoup import *

str = raw_input("Enter the link ")

html = urllib.urlopen(str).read()

bsoup = BeautifulSoup(html)

tags = bsoup('a')

for tag in tags:
    print tag.get('href', None)
