#!/usr/local/bin python
#coding=utf-8
#author: Zheng Qin
#desc: Read price from schema html page.
#-----------------------
#2013-03-07 created

#----------------------

import urllib2
# from lxml import *
import lxml.etree as etree

# html = '''

# <html>
# 　　<head>
# 　　</head>
# 　　<body>
# 　　　　<h1 class="heading">Top News</h1>
# 　　　　<p style="font-size: 200%">World News only on this page</p>
# 　　　　Ah, and here's some more text, by the way.
# 　　　　<p>... and this is a parsed fragment ...</p>

# 		<div class="price hilight" itemprop="price" data-bntrack="Price" data-bntrack-event="click">$19.99</div>
#         <div class="price-info">

# 　　</body>
# </html>

# '''

# page = etree.HTML(html.lower().decode('utf-8'))

# hrefs = page.xpath("//div")

# for href in hrefs:
# #	print href.attrib
# 	if href == ("itemprop="price"")
# 	print href.text



def get_all_prices(url):
	# get root node
	urlopener = urllib2.urlopen(url)
	page_html = urlopener.read()
	page = etree.HTML(page_html.lower().decode('utf-8'))
	prices = page.xpath('//*[@itemprop="price"]')
	# names = page.xpath('//*[@itemprop="name"]')


	for price in prices:
		print price.text

	# for name in names:
	# 	print name.text

	# prices = []

	# parser = etree.HTMLParser(encoding='utf8')
	# mytree= etree.parse(f,parser)


# <span id="bb_bdp">
# 	<span id="prcIsum" style="" class="" itemprop="price">US $99.99</span>
# </span>
	# dom = etree.fromstring(page_html)
	# print dom.xpath('//*[@itemprop="price"]')[0].text

	# searchString = doc.xpath('//*[@itemprop="price"]')


# <span itemprop="availability" content="http://schema.org/OnlineOnly"></span>
# 	<span itemprop="priceCurrency" content="USD">
# </span>
	# for i in searchString:
		# tmp = i.text_content()
		# prices.append(tmp)

# got all the prices of the page
	# return prices


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
#     table = root.getElementsByTagName("table")[0]

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
	'http://www.barnesandnoble.com/p/home-gift-ihome-colortunes-noise-isolating-headphones-black/25210773?ean=47532897302&isbn=47532897302',
	'http://www.barnesandnoble.com/p/home-gift-ihome-ib40b-over-the-ear-headphones-with-volume-control-black/22201677?ean=47532895629&isbn=47532895629',
	'http://www.barnesandnoble.com/p/home-gift-portable-stereo-speaker-system-in-black/25550011?ean=47532895520&isbn=47532895520',
	'http://www.barnesandnoble.com/p/elan-passport-wallet-for-iphone-4-in-platinum-with-lanyard/25218472?ean=685387307999&isbn=685387307999',
	'http://www.barnesandnoble.com/p/home-gift-bookbook-case-for-iphone-4-4s-classic-black/25390388?ean=851522002429&isbn=851522002429'
	]

	# outfile = open(‘schemaPrices.txt’, ‘w’)
	for url in urls:
		products = get_all_prices(url)



	# outfile.close()
