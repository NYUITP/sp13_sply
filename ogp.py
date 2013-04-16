#!/usr/local/bin python
# coding=utf-8

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


def is_url_opg(page):
    flag = page.xpath('//meta[@name="description"]')
    result = 1
    if (flag == []):
        result = 0
    return result


def get_product_price(page):
    prices = page.xpath('//*[@itemprop ="price"]')
    if prices != []:
        price = prices[0]
    else:
        prices = page.xpath('//*[@class="active_price"]')
        if prices != []:
            price = prices[0]
        else:
            prices = page.xpath('//*[@class="price"]')
            if prices != []:
                price = prices[0]
            else:
                prices = page.xpath('//*[@class="sale-price"]')
                price = prices[0]
                # class="sale-price"

    price = prices[0]
    return filter(lambda ch: ch in '€￥£円$0123456789.,', price.text)


if __name__ == '__main__':
    file = open('good_urls.txt')
    while 1:
        urls = file.readlines(100000)
        if not urls:
            break
        for url in urls:
            # print url
            if is_url_available(url):
                page = urlreader(url)
                try:
                    if is_url_opg(page):
                        # print "###############################################################"
                        # print url,
                        # print "****************************************************************"
                        print get_product_price(page)
                except Exception, e:
                    print e.__class__,  e, url
