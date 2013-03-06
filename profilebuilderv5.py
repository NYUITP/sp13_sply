#!/usr/bin/env python
import json
from lxml import etree
import urllib


myjsonfile = open('validated_products.json')
for line in myjsonfile:
	json_map = json.loads(line)
	#print json_map

opener = urllib.FancyURLopener({})
f = opener.open(json_map["url"])

VPRICE=json_map["price"] #VALIDATED PRICE
parser = etree.HTMLParser(encoding='utf8')
mytree= etree.parse(f,parser)
XPATH_SEARCH_STRING = '//*[text()="' + VPRICE + '"]' 
myelements_locations = mytree.xpath(XPATH_SEARCH_STRING)
myresults=[]
for Elem_location in myelements_locations:
	myresults.append(mytree.getpath(Elem_location))
 	## To verify
for resul in myresults:
	search= resul + '/text()'
print "{\"domain\": \"%s\",\"url\": \"%s\",\"xpath\": \"%s\"}" % (json_map["domain"],json_map["url"],search)
f.close()
myjsonfile.close()
