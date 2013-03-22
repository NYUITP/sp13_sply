#!/usr/local/bin python
#coding=utf-8

from bottle import route, run
from pprint import pprint
import urllib2
import lxml.etree as etree
import httplib
import urlparse

@route('/schema/<weburl:path>')

def schema(weburl):
	if is_url_available(weburl):
		if is_url_schema(weburl):
			print (get_product_name(weburl) + " is " + get_product_price(weburl))
			# print get_product_price(url)
			print " "
		else:
			print ("***"+weburl+"***  ")
			print "This is not a Schema type website!"
			print " "
	else:
		print "URL not exists"
		print " "

	


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



def is_url_schema(url):

	flag = urlreader(url).xpath('//*[@itemprop="name"]')

	result = 1

	if (flag == []):
		result = 0

	return result



def urlreader(url):
	page_html = urllib2.urlopen(url).read()
	page = etree.HTML(page_html.lower().decode('utf-8'))
	return page


def get_product_price(url):
	
	prices = urlreader(url).xpath('//*[@itemprop="price"]')
	price = prices[0]

	return price.text



def get_product_name(url):

	names = urlreader(url).xpath('//*[@itemprop ="name"]')

	name = names[0]

	return name.text


run (host='localhost',port = 8080, debug = True)
