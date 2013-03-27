#!/usr/local/bin python
#coding=utf-8

from bottle import route, run
from pprint import pprint
import urllib2
import lxml.etree as etree
import httplib
import urlparse

@route('/schema/<url:path>')

# def schema(url):
	# if is_url_available(url):
	# 	page = urlreader(url)
	# 	if is_url_schema(page):
	# 		print (get_product_name(page) + " is " + get_product_price(page))
	# 		# print get_product_price(url)
	# 		print " "
	# 	else:
	# 		print ("***"+weburl+"***  ")
	# 		print "This is not a Schema type website!"
	# 		print " "
	# else:
	# 	print "URL not exists"
	# 	print " "

def schema(url):
	if is_url_available(url):
		page = urlreader(url)
		if is_url_schema(page):
			if is_url_instock(page):
				# print (get_product_name(page) + " is " + get_product_price(page))
				# print " "
				product_name = get_product_name(page)
				product_price = get_product_price(page)
				return product_name + " is " + product_price
			# elif is_product_onsale(page):
			# 	print (get_product_name(page) + " is ON SALE!! The on sale price is " + get_onsale_price(page))
			# 	print " "
			else:
				if is_product_onsale(page):
					# print (get_product_name(page) + " is ON SALE!! The on sale price is " + get_onsale_price(page))
					# print " "
					product_name = get_product_name(page)
					onsale_price = get_onsale_price(page)
					return product_name + " is ON SALE!! The on sale price is " + onsale_price
				else:
					# print (get_product_name(page)+" is out of stock!")
					# print " "
					product_name = get_product_name(page)
					return product_name + " is out of stock!"
		else:
			# print ("***"+url+"***  ")
			# print "This is not a Schema type website!"
			# print " "
			return "This is not a Schema type website!"
	else:
		# print "URL not exists"
		# print " "
		return "URL not exists"


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

def is_product_onsale(page):
	flag = page.xpath('//*[@id="ourprice"]')
	result = 1
	if (flag == []):
		result = 0
	return result

def get_onsale_price(page):
	prices = page.xpath('//*[@id="ourprice"]')
	price = prices[0]
	return price.text.strip()

def get_product_price(page):
	prices = page.xpath('//*[@itemprop="price"]')
	price = prices[0]
	return price.text.strip()

def get_product_name(page):
	names = page.xpath('//*[@itemprop ="name"]')
	name = names[0]
	return name.text.strip()


run (host='localhost',port = 8082, debug = True)
