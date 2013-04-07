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
# run (host='localhost',port = 8080, debug = True)


def get_price(weburl):
    final = []
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    f = opener.open(weburl)
    s = f.read()
    s = unicode(s, 'utf-8')
    f.close()
    hdoc = HTML.fromstring(s)
    htree = etree.ElementTree(hdoc)
    # search xpath contain currency symbol
    key = xpath_filter()
    key_locations = htree.xpath("//*[re:match(text(),'"+key+"')]", namespaces={"re": "http://exslt.org/regular-expressions"})
    keyresults = []
    truexpath = ""
    currency = ""
    for Elem_location in key_locations:
        keyresults.append(htree.getpath(Elem_location))

    # get price and currency

    for result in keyresults:
        truexpath = result
        if truexpath.find('script') == -1:
            # print truexpath
            locations = htree.xpath(truexpath)
            # truexpath= truexpath[truexpath.find("\'")+1:truexpath.rfind("\'")]
            for Elem_location in locations:
                price = Elem_location.text
                if price != None:
                    flag = price_check(price)
                    # print flag
                    if flag == False:
                        final.append(price_get(price, truexpath))
                    else:
                        truexpath = truexpath[:truexpath.rfind('/')+1]+"*"
                        locations = htree.xpath(truexpath)
                        # locations = htree.xpath("/html/body/div[2]/section/section/div[2]/p[1]/span")

                        for Elem_location in locations:
                            price = Elem_location.text
                            if price != None:
                                final.append(price_get(price, truexpath))

    print final[0]
    return final


def xpath_filter():
    currencyhead = "€|￥|£|$"
    curhead = "[€,￥,£,$]"
    curhead = unicode(curhead, 'utf-8')
    currencyhead = unicode(currencyhead, 'utf-8')
    currencytail = "EUR|Euro|RMB|RBP|JPY|CAD|AUD|USD"
    numberstring = "\\d+(?:(?:\\.|,)\\d\\d)?"
    # key = "\\s*?(?:"+currencyhead+")?\\s*"+numberstring+"\\s*(?:"+currencytail+")+?\\s*?"
    key = "^"+currencyhead+""+numberstring+""+currencytail+"$"
    return key


def price_check(price):
    currencytail = "EUR|Euro|RMB|RBP|JPY|CAD|AUD|USD"
    curhead = "[€,￥,£,$]"
    curhead = unicode(curhead, 'utf-8')
    flag = False
    reg4 = curhead+"?.[0-9\,\.]{1,}"
    m4 = re.search(reg4, price)
    reg5 = "^[0-9\.\,]{1,}?.("+currencytail+")$"
    m5 = re.search(reg5, price)
    reg6 = "^"+curhead+"[0-9\,\.]{1,}("+currencytail+")$"
    m6 = re.search(reg6, price)
    reg1 = "^"+curhead+"$"
    m1 = re.search(reg1, price)
    reg2 = "^("+currencytail+")$"
    m2 = re.search(reg2, price)
    reg3 = "^"+curhead+"."+"("+currencytail+")$"
    m3 = re.search(reg3, price)
    '''
    if  m4!=None:
        print "m4" + m4.group(0)
    elif m5!=None:
        print "m5" + m5.group(0)
    elif m6!=None:
        print "m6" + m6.group(0)
    '''
    if m1 != None:
        flag = True
        # print "m1" + m1.group(0)
    elif m2 != None:
        flag = True
        # print "m2" + m2.group(0)
    elif m3 != None:
        flag = True
        # print "m3" + m3.group(0)
    else:
        # print "some else"
        flag = False
        # print price
    return flag


def price_get(pri, xpath):
    currency = ""
    price = ""
    symbol = ""
    strflag = False

    pricetem = pri.split()
    for tem in pricetem:
        print tem
        m1 = re.search('^[0-9\.\,]{1,}$', tem)
        if m1 != None:
            strflag = True
            price = tem
    if strflag == True:
        for tem in pricetem:
            m2 = re.search('^[A-Za-z]{1,}$', tem)
            m3 = re.search('^\$$', tem)
            if m2 == None:
                if m3 != None:
                    symbol = tem
                # else:
                    # print "not price"
            else:
                currency = tem
    else:
        for tem in pricetem:
            m4 = re.search('^.[0-9\.\,]{1,}$', tem)
            if m4 != None:
                symbol = tem[:1]
                price = tem[1:]
            print price

    return (symbol, currency, price, xpath)


# url="http://www.oipolloi.com/apc-cable-knit-pullover-off-white",
# url="http://www.urbanoutfitters.com/urban/catalog/productdetail.jsp?id=26503334&parentid=M_APP_SHORTSSWIM_SHORTS"
# url="http://www.urbanoutfitters.com/urban/catalog/category.jsp?id=BRANDS&brand=rothco"
# url="http://www.freepeople.com/whats-new-intimates/"
# url = "http://www.manufactum.com/sweaters-c193633/"
# url = "http://www.etsy.com"
url ="http://www.urbanoutfitters.com/urban/catalog/category.jsp?id=BRANDS&brand=rothco"
# url="http://www.zara.com/webapp/wcs/stores/servlet/category/us/en/zara-nam-S2013/358080/Jackets"
# url="http://www.zara.com/webapp/wcs/stores/servlet/product/us/en/zara-nam-S2013/358082/1224520/POLKA+DOT+DRESS"
# url = get_price(url)
