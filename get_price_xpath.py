# from bottle import route, run
import lxml.html as HTML
import lxml.etree as etree
import difflib
from difflib import SequenceMatcher
import urllib2
import cookielib
from pprint import pprint
import re
#@route('/xpath/<weburl:path>,<imgurl:path>')


def get_price(weburl):
    keywordlist = ['Euro', 'euro', 'USD', '$', 'RMB']
    keyresults = []
    truexpath = ""
    results = []
    price = []
    currency = ""
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))

    f = opener.open(weburl)
    s = f.read()
    f.close()

    hdoc = HTML.fromstring(s)
    htree = etree.ElementTree(hdoc)

    for keyword in keywordlist:
        key_locations = htree.xpath("//*[re:match(text(),'"+keyword+"')]", namespaces={
                                    "re": "http://exslt.org/regular-expressions"})
        for Elem_location in key_locations:
            keyresults.append(htree.getpath(Elem_location))

        if len(keyresults) != False:
            currency = keyword
            break

    flag = False
    for result in keyresults:
        truexpath = result
        locations = htree.xpath(truexpath)

    for Elem_location in locations:
        results.append(htree.getpath(Elem_location))
        price.append(Elem_location.text)
        print Elem_location.text
        pricestr = str(price)

    pricestr = pricestr[pricestr.find("\'")+1:pricestr.rfind("\'")]
    if pricestr.isdigit() == True:
        flag = True
        productprice = pricestr
    elif pricestr.isalpha() == True:
        flag = True
    else:
        flag = False
        pricetem = pricestr.split()
        for tem in pricetem:
            if tem.find(',') > -1:
                productprice = tem
            elif tem.find('.') > -1:
                productprice = tem
                break

    if flag == True:
        truexpath = truexpath[:truexpath.rfind('/')-1]
        truexpath = truexpath+'*'
        # truexpath = "/html/body/div[6]/div/div/div/div[2]/div[1]/div[1]/div[2]/*"
        locations = htree.xpath(truexpath)
        for Elem_location in locations:
            results.append(htree.getpath(Elem_location))
            price.append(Elem_location.text)
            print Elem_location.text
        pricetem = str(price).split()
        for tem in pricetem:
            tem = tem[tem.find("\'")+1:tem.rfind("\'")]
            # print tem
            if tem.isalpha() == False and tem.find(".") > -1:
                productprice = tem
                break
            elif tem.isalpha() == False and tem.find(",") > -1:
                productprice = tem
                break

    print "pricexpath " + truexpath
    return truexpath


# run (host='localhost',port = 8080, debug = True)
url = "http://www.manufactum.com/sweaters-c193633/"
get_price(url)
