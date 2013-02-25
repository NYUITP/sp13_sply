#!/usr/bin/env python
import json
from lxml import etree
import urllib


myprofiles = open('created_profiles.json')
prof={}
for line in myprofiles:
 json_map = json.loads(line)
 prof[json_map["domain"]] = json_map["xpath"]
myprofiles.close()
print prof

unvalidate_file = open('unvalidated_products.json')
for line in unvalidate_file:
 json_map=json.loads(line)
 if prof.has_key(json_map["domain"]):
  opener = urllib.FancyURLopener({})
  f = opener.open(json_map["url"])
  parser = etree.HTMLParser(encoding='utf8')
  mytree= etree.parse(f,parser)
  f.close()
  print "URL: %s, DBPrice: %s, CurrentPrice: %s"  % (json_map["url"], json_map["price"],mytree.xpath(prof[json_map["domain"]]))





unvalidate_file.close()

