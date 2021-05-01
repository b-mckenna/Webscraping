#Scraps the completed tasks from any.do

import urllib
from BeautifulSoup import *

url = 'https://desktop.any.do/tasks/today?d=anydo%3A%2F%2Fanydo%3Faction%3Dtasktab'

html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)
tags = soup.findAll('<head>')
print(tags)
lst = list()
for line in tags:
    newLine = unicode.join(u'\n',map(unicode,line)).encode('ascii', 'ignore')
    lst += re.findall('class="(.*?)"',newLine)

print lst
