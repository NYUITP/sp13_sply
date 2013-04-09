#!/usr/local/bin python
# coding=utf-8


import urllib2
import lxml.etree as etree
import httplib
import urlparse


def get_price(url):
    page = urlreader(url)
    return (get_product_name(page) + " is " + get_product_price(page))


def urlreader(url):
    page_html = urllib2.urlopen(url).read()
    page = etree.HTML(page_html.lower())
    return page


def is_url_available(url):
    host, path = urlparse.urlsplit(url)[1:3]
    found = 0
    try:
        connection = httplib.HTTPConnection(host)  # Make HTTPConnection Object
        connection.request("HEAD", path)
        responseOb = connection.getresponse()  # Grab HTTPResponse Object

        if responseOb.status == 200:
            found = 1
        else:
            print "Status %d %s : %s" % (responseOb.status, responseOb.reason, url)
    except Exception, e:
        print e.__class__,  e, url
    return found


# def is_url_schema(page):
#     flag = page.xpath('//*[@itemprop="name"]')
#     result = 1
#     if (flag == []):
#         result = 0
#     return result


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


def helloworld():
    return "Hello World!"


# Read solution from json file
def get_solution():
    pass
