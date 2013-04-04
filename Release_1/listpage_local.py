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


def xpath(weburl, imgurl):
    keywordlist = ['Euro', 'USD', '$', 'RMB']
    statuslist = ['in stock', 'available']
    kclosest = 0
    sclosest = 0
    imgresults = []
    keyresults = []
    statusresults = []
    imgxpath = ""
    matchfirst = []
    truexpath = ""
    results = []
    price = []
    finalstatus = []
    currency = ""
    productprice = ""
    productstatus = ""
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    # weburl = "http://"+weburl

    f = opener.open(weburl)
    s = f.read()
    f.close()

    hdoc = HTML.fromstring(s)
    htree = etree.ElementTree(hdoc)
    # imgurl = "http://"+imgurl
    image_locations = htree.xpath('//img[@src="'+imgurl+'"]')

    if len(image_locations) == False:
        print "no image"

    for Elem_location in image_locations:
        imgresults.append(htree.getpath(Elem_location))
    for result in imgresults:
        imgxpath = result
        # print imgxpath

    for keyword in keywordlist:
        key_locations = htree.xpath("//*[re:match(text(),'"+keyword+"')]", namespaces={
                                    "re": "http://exslt.org/regular-expressions"})
        for Elem_location in key_locations:
            keyresults.append(htree.getpath(Elem_location))
        if len(keyresults) != False:
            currency = keyword
            break

    for result in keyresults:
        # keyxpath = result
        s = difflib.SequenceMatcher(None, imgxpath, result)
        matchfirst = s.get_matching_blocks()[0]
        close_degree = matchfirst[2]
        if kclosest < close_degree:
            kclosest = close_degree
            truexpath = result

    flag = False
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
        truexpath = truexpath[:truexpath.rfind('/')]
        truexpath = truexpath+'/*'
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

    for status in statuslist:
        status_locations = htree.xpath("//*[re:match(text(),'"+status+"')]", namespaces={
                                       "re": "http://exslt.org/regular-expressions"})
        for Elem_location in status_locations:
            statusresults.append(htree.getpath(Elem_location))
        if len(statusresults) != False:
            productstatus = status
            break
    sxpath = ""
    for result in statusresults:
        status_xpath = result
        s = difflib.SequenceMatcher(None, imgxpath, status_xpath)
        matchfirst = s.get_matching_blocks()[0]
        close_degree = matchfirst[2]
        if sclosest < close_degree:
            sclosest = close_degree
            sxpath = status_xpath

    if len(sxpath) != False:
        statuslocations = htree.xpath(sxpath)
        for Elem_location in statuslocations:
            finalstatus.append(Elem_location.text)
            print Elem_location.text

    else:
        print "can't get status"
        finalstatus = ""

    print "pricexpath " + truexpath
    print "statusxpath " + sxpath
    return truexpath, sxpath
    # return  productprice+productstatus


# run (host='localhost',port = 8080, debug = True)

imgurl = "http://images.manufactum.de/manufactum/thumbs_188/20415_1.jpg"
imgurl1 = "http://img2.etsystatic.com/006/0/5755013/il_170x135.372291786_3e5a.jpg"
# weburl = "http://www.manufactum.com/outerwear-c193631/"
weburl = 'http://www.manufactum.com/horse-leather-gentlemans-blouson-p1464993/?c=193631'
weburl1 = "http://www.etsy.com/"
xpath(weburl, imgurl)
