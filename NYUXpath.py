#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from get_price_test import get_price
from imagexpath_get import xpath_imgrequest
from xpath_compare import xpath_compare
from get_price_test import price_get
from get_price_test import currency_get
import json

def main_process(weburl, imgurl):
    
    urls = []
    results = []
    finprice = {}
    fincurrency = {}
    results = get_price(weburl)
    for result in results:
        finprice.update({result[2]:result[1]})
        fincurrency.update({result[2]:result[0]})
        urls.append(result[2])

    imgxpath = xpath_imgrequest(imgurl,weburl)
    close_xpath=[]
    close_xpath = xpath_compare(imgxpath, urls)

#    for xpath in close_xpath:
#        print finprice[xpath]
#        print fincurrency[xpath]
#        print xpath
    return  json.dumps({"price": finprice[close_xpath[0]], "currency": fincurrency[close_xpath[0]], "xpath": close_xpath[0]})      

if __name__ == "__main__":

 #weburl2="http://www.modcloth.com/shop/dresses/jumpsuit-yourself-romper-in-plus-size"
 #imgurl2="http://productshots0.modcloth.com/productshots/0127/3869/aca2b9a0adc41fe50d5b7950e2f19d3c.jpg?1364852451"
 #weburl2="http://www.insound.com/Pipe-Earphones-w-Mic-Petroleum-Gradient-Headphones-AIAIAI/P/INS114166/"
 #imgurl2="http://s3.amazonaws.com/images.insound.com/303/INS114166.gif"
 #print main_process(weburl2, imgurl2)
 myfile = open('schema_urls.txt')
 for line in myfile:
   (weburl, imgurl) = line.split('\t')
   #print weburl.rstrip()
   print main_process(weburl,imgurl)
 myfile.close()
