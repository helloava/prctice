#-*- coding: utf-8 -*-

import urllib2

def ed(pgNum):
	a=urllib2.urlopen('https://www.edx.org/course-list?page=%d'%(pgNum))
	html=a.read().split('<div class="top views-fieldset" data-module="views_fieldsets">')

	for data in html[1:]:
		print data.split('</a>')[0]

for i in range(1,9):
	ed(i)