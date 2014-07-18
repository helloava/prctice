import urllib

from bs4 import BeautifulSoup

htmltext = urllib.urlopen("http://hbr.org/").read()

soup = BeautifulSoup(htmltext)

authors = []

for tag in soup.select(".item-title"):
	authors.append(tag.get_text())
for author in authors:
	print author

