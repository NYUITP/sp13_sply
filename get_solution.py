#!/usr/local/bin python
# coding=utf-8


import urllib2
import lxml.etree as etree
import httplib
import urlparse


# def get_solution(url):
#     page = urlreader(url)
#     return (get_product_name(page) + " is " + get_product_price(page))


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


if __name__ == '__main__':
    urls = {
        'http://www.modcloth.com/shop/handbags/a-coast-call-bag',
        'http://store.apple.com/us/browse/home/shop_mac/family/mac_pro?mco=MjI4NDU1',
        'http://www.modcloth.com/shop/kitchen-gadgets/talented-mr-apple-bottle',
        'http://www.insound.com/Y-Com-Earphones-with-Microphone-Grey-Headphones-AIAIAI/P/INS52376/',
        'http://www.overstock.com/Luggage-Bags/Floto-Leather-Venezia-Leather-Duffel-Bag/3821244/product.html?sec_iid=33%20969',
        'http://www.barnesandnoble.com/p/home-gift-homer-and-aristotle-cast-marble-bookends-set-of-2/12601703?ean=9780830078097&isbn=9780830078097',
        'http://www.bbq.com/item_name_Smokin-Tex-1400-Pro-Series-Electric-BBQ-Smoker_path_7119-7122_item_1530808.html'
    }

    for url in urls:
        if is_url_available(url):
            page = urlreader(url)
            if is_url_schema(page):
                print url
                if is_url_instock(page):
                    # print (get_product_name(page) + " is " + get_product_price(page))
                    print get_product_price(page)
                    print " "
                # elif is_product_onsale(page):
                #   print (get_product_name(page) + " is ON SALE!! The on sale price is " + get_onsale_price(page))
                #   print " "
                else:
                    if is_product_onsale(page):
                        # print (get_product_name(page) + " is ON SALE!! The on sale price is " + get_onsale_price(page))
                        print get_onsale_price(page)
                        print " "
                    else:
                        # print (get_product_name(page)+" is out of stock!")
                        print "$9999999999999999"
                        print " "
            else:
                print ("***"+url+"***  ")
                print "This is not a Schema type website!"
                print " "
        else:
            print "URL not exists"
            print " "
