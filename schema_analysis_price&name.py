#!/usr/local/bin python
#coding=utf-8

import urllib2
import lxml.etree as etree
import httplib
import urlparse

def urlreader(url):
	page_html = urllib2.urlopen(url).read()
	page = etree.HTML(page_html.lower())
	return page

def is_url_available(url):
	host, path = urlparse.urlsplit(url)[1:3]
	found = 0
	try:
		connection = httplib.HTTPConnection(host)  ## Make HTTPConnection Object
		connection.request("HEAD", path)
		responseOb = connection.getresponse()      ## Grab HTTPResponse Object

		if responseOb.status == 200:
			found = 1
		else:
			print "Status %d %s : %s" % (responseOb.status, responseOb.reason, url)
	except Exception, e:
		print e.__class__,  e, url
	return found

def is_url_schema(page):
	flag = page.xpath('//*[@itemprop="name"]')
	result = 1
	if (flag == []):
		result = 0
	return result

def is_url_instock(page):
	flag = page.xpath('//*[@itemprop="price"]')
	result = 1
	if (flag == []):
		result = 0
	return result

def get_product_price(page):
	prices = page.xpath('//*[@itemprop="price"]')
	price = prices[0]
	return price.text.strip()

def get_product_name(page):
	names = page.xpath('//*[@itemprop ="name"]')
	name = names[0]
	return name.text.strip()


# check if the url is a schema style
# def if_schema_page(url):
# 	pass

# get the domain name of a url
# def get_domain_name():
# 	pass

# connect to the database and get 
# def load_dbconnected_profile(domain_name):
#     content = {}

#     root = minidom.parse(<span style="background-color: rgb(255, 255, 255); ">domain_name</span>)
#     table = root.getElementsByTagName("table")[0]∫

#   #read dbname and table name.
#     table_name = table.getAttribute("name")
#     db_name = table.getAttribute("db_name")

#     if len(table_name) > 0 and len(db_name) > 0:
#      db_sql = "create database if not exists `" + db_name +"`; use " + db_name + ";" 
#      table_drop_sql = "drop " + table_name + " if exists " + table_name + ";" 
#      content.update({"db_sql" : db_sql})
#      content.update({"table_sql" : table_drop_sql })
#   else:
#      print "Error:attribute is not define well!  db_name=" + db_name + " ;table_name=" + table_name
#      sys.exit(1)

if __name__ == '__main__':
	urls = [
	'http://www.barnesandnoble.com/p/home-gift-ihome-ihm60-20-rechargable-mini-speaker-gray/25547311?ean=47532896213&isbn=47532896213&urlkeywords=ihome+ihm60+20+rechargable+mini+speaker+gray',
	'http://www.barnesandnoble.com/p/toys-games-kiss-8-gb-usb-flash-drive-peter-criss-catman/25209496?ean=895221380051&isbn=895221380051',
	'http://www.bbq.com/item_name_Kamado-Joe-ClassicJoe-Ceramic-Kamado-Grill-On-Cart-Red_path_2112-11447_item_2854890',
	'http://www.barnesandnoble.com/p/home-gift-ihome-colortunes-noise-isolating-headphones-black/25210773?ean=47532897302&isbn=47532897302',
	'http://www.manufactum.com/maplewood-foldable-wardrobe-p1465202/'
	'http://www.barnesandnoble.com/p/home-gift-ihome-ib40b-over-the-ear-headphones-with-volume-control-black/22201677?ean=47532895629&isbn=47532895629',
	'http://www.barnesandnoble.com/p/home-gift-portable-stereo-speaker-system-in-black/25550011?ean=47532895520&isbn=47532895520123123123',
	'http://www.manufactum.com/devold-nansen-troyer-style-pullover-p1465134/',
	'http://www.barnesandnoble.com/p/elan-passport-wallet-for-iphone-4-in-platinum-with-lanyard/25218472?ean=685387307999&isbn=685387307999',
	'http://www.bbq.com/item_name_Kamado-Joe-ClassicJoe-Ceramic-Kamado-Grill-On-Cart-Red_path_9994_item_2854890.html'
	]


	# outfile = open(‘schemaPrices.txt’, ‘w’)
	for url in urls:
		if is_url_available(url):
			page = urlreader(url)
			if is_url_schema(page):
				if is_url_instock(page):
					print (get_product_name(page) + " is " + get_product_price(page))
					print " "
				else:
					print (get_product_name(page)+" is out of stock!")
					print " "
			else:
				print ("***"+url+"***  ")
				print "This is not a Schema type website!"
				print " "
		else:
			print "URL not exists"
			print " "
