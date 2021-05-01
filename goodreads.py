#Scraps all the books I've read from Goodreads.com using BeautifulSoup3

import urllib
from BeautifulSoup import *
from pprint import pprint as pp

url = 'https://www.goodreads.com/review/list/23319857-brendan-mckenna?shelf=read'
html = urllib.urlopen(url).read()

tags = soup.findAll('td','field title','a')
lst = list()
for line in tags:
    newLine = unicode.join(u'\n',map(unicode,line)).encode('ascii', 'ignore')
    lst += re.findall('title="(.*?)"',newLine)

print("<---------------------Books Brendan has Read---------------------->") 
for i in lst:
    pp(i);
