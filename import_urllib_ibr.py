#-*- coding: utf-8 -*-

import urllib2 

def ent_title(pageNum):
	ent=urllib2.urlopen('http://ibr.kr/category/entrepreneurship/page/%d'%(pageNum))
	html = ent.read().split('<article class="item-list">')

	for data in html[1:]: 
	 	print data.split('</a>')[0].split('">')[2].decode("utf-8") 
		#print toon
for i in range(1,3) :
	ent_title(i)