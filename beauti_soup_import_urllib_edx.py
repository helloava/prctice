import urllib

from bs4 import BeautifulSoup

htmltext = urllib.urlopen("https://www.edx.org/course-list").read()

soup = BeautifulSoup(htmltext)

authors = []

for tag in soup.select(".new-course-ribbon"):
	authors.append(tag.get_text())
for author in authors:
	print author

