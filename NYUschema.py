#!/usr/bin/env  python
# coding=utf-8


import urllib2
import lxml.etree as etree
import httplib
import urlparse
import json


def get_solution(url):
    page = urlreader(url)
    if is_url_schema(page):
        myprice = get_price(page)
    elif is_url_opg(page):
        myprice = get_ogp_price(page)
    else:
        print "-2"
    return myprice

def get_price(page):
    # print url
    # page = urlreader(url)
    # if is_url_instock(page):
    #     myprice = get_product_price(page)
    # elif is_product_onsale(page):
    #     myprice = get_onsale_price(page)
    # elif is_sub_price(page):
    #     myprice = get_sub_price(page)
    # else:
    # myprice = "-1"  # out of stock
    # page = urlreader(url)
    if is_sub_price(page):
        myprice1 = get_sub_price(page)
    elif is_url_instock(page):
        myprice1 = get_product_price(page)
    elif is_product_onsale(page):
        myprice1 = get_onsale_price(page)
    else:
        myprice1 = "-1"  # out of stock
    return myprice1


def get_ogp_price(page):
    # page = urlreader(url)
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

    # price = prices[0]
    return filter(lambda ch: ch in '€￥£$0123456789.,', price.text)


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


def is_url_opg(page):
    flag = page.xpath('//meta[@name="description"]')
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


def is_sub_price(page):
    flag = page.xpath('//*[@class="amount"]')
    result = 1
    if (flag == []):
        result = 0
    return result


def get_onsale_price(page):
    prices = page.xpath('//*[@id="ourprice"]')
    price = prices[0]
    return filter(lambda ch: ch in '€￥£$0123456789.,', price.text)
    # return price.text.strip()


def get_sub_price(page):
    prices = page.xpath('//*[@class="amount"]')
    price = prices[0]
    return filter(lambda ch: ch in '€￥£$0123456789.,', price.text)
    # return price.text.strip()


def get_product_price(page):
    prices = page.xpath('//*[@itemprop="price"]')
    price = prices[0]
    # €,￥,£,$,円
    return filter(lambda ch: ch in '€￥£円$0123456789.,', price.text)
    # filter(str.isalnum, crazystring)
    # return price.text.strip()


def get_product_name(page):
    names = page.xpath('//*[@itemprop ="name"]')
    name = names[0]
    return name.text.strip()


if __name__ == '__main__':
    '''
      urls = {
           'http://www.modcloth.com/shop/handbags/a-coast-call-bag',
           'http://store.apple.com/us/browse/home/shop_mac/family/mac_pro?mco=MjI4NDU1',
           'http://www.modcloth.com/shop/kitchen-gadgets/talented-mr-apple-bottle',
           'http://www.insound.com/Y-Com-Earphones-with-Microphone-Grey-Headphones-AIAIAI/P/INS52376/',
           'http://www.overstock.com/Luggage-Bags/Floto-Leather-Venezia-Leather-Duffel-Bag/3821244/product.html?sec_iid=33%20969',
           'http://www.barnesandnoble.com/p/home-gift-homer-and-aristotle-cast-marble-bookends-set-of-2/12601703?ean=9780830078097&isbn=9780830078097',
           'http://www.bbq.com/item_name_Smokin-Tex-1400-Pro-Series-Electric-BBQ-Smoker_path_7119-7122_item_1530808.html'
       }

    #    for url in urls:
    #        if is_url_available(url):
    #            print get_solution(url)
    #   '''
    myfile = open('schema_urls_org.txt')
    for line in myfile:
        # (weburl, imgurl) = line.split('\t')
        # print weburl.rstrip()
        weburl = line`
        print weburl
        page = urlreader(weburl)
        if is_url_schema(page):
            print get_price(page)
        elif is_url_opg(page):
            print get_ogp_price(page)
        else:
            print "-2"
        # print get_solution(weburl)
    myfile.close()
    # url = 'http://store.hypebeast.com/brands/undefeated/olive-play-dirty-new-era-beanie'
    # page = urlreader(url)
    # print is_product_onsale(page)
    # print is_url_instock(page)
    # print is_sub_price(page)
    # print get_product_price(page)
    # print get_sub_price(page)
