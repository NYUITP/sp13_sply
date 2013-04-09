#from bottle import route, run
import lxml.html as HTML
import lxml.etree as etree
import difflib
from difflib import SequenceMatcher
import urllib2
import cookielib
from pprint import pprint
import  re
from price_check import price_check
from price_get import price_get
from xpath_filter import xpath_filter
from currency_get import currency_get
#@route('/xpath/<weburl:path>,<imgurl:path>')
#run (host='localhost',port = 8080, debug = True)

def get_price(weburl):
    final_list = []    
    keyresults=[]
    truexpath = ""
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    f = opener.open(weburl)
    s = f.read()
    s = unicode(s, 'utf-8')
    f.close()
    hdoc = HTML.fromstring(s)
    htree = etree.ElementTree(hdoc)
    #search xpath contain currency symbol
    keys = xpath_filter()
    for key in keys:
        key_locations = htree.xpath("//*[re:match(text(),'"+key+"')]", namespaces={"re": "http://exslt.org/regular-expressions"})
        for Elem_location in key_locations:
            keyresults.append(htree.getpath(Elem_location))
        if len(keyresults)!=False:
            break
         
    # get price and currency
    
    for result in keyresults:
        truexpath = result
        final_currency=""
        final_price= ""
        final_symbol=""
        if truexpath.find('script')==-1: 
             #print truexpath
             modxpath = []
             
             modxpath.append(truexpath[:truexpath.rfind('/')+1]+"*")
             modxpath.append(truexpath[:truexpath.rfind('/')])
             temxpath = truexpath[:truexpath.rfind('/')]
             modxpath.append(temxpath[:temxpath.rfind('/')+1]+"*")
             modxpath.append(temxpath[:temxpath.rfind('/')])
             
             flag = False
             locations = htree.xpath(truexpath)
             for Elem_location in locations:
                 price = Elem_location.text
                 if price!=None:
                    final_currency = currency_get(price)
                    flag = price_check(price)
                    #print flag
                    #print price
                    if flag == False:
                        if price_get(price)!= "No price" and price_get(price)!= None:
                            final_price = price_get(price)
                        
                    else:
                        break
             if flag == True:
                 for mod in modxpath:
                     loc = htree.xpath(mod)              
                     for Elem_location in loc:
                        price = Elem_location.text
                        price_get(price)
                        #print price
                        if price_get(price)!="No price":
                            final_price = price_get(price)
                            break
                     
               
        final =[]
        
        #print final_currency
        #print final_price
        final.append(final_currency)
        final.append(str(final_price))
        final.append(truexpath)
        final_list.append(final)
    #print final_list
    return final_list
        

    

    


    

            
url="http://www.oipolloi.com/apc-cable-knit-pullover-off-white"
url="http://www.urbanoutfitters.com/urban/catalog/productdetail.jsp?id=26503334&parentid=M_APP_SHORTSSWIM_SHORTS"
url = "http://www.urbanexcess.com/c-1190-sweatshirts.aspx"
url="http://www.freepeople.com/whats-new-intimates/"
url = "http://www.manufactum.com/sweaters-c193633/"
url = "http://www.etsy.com"
url ="http://www.urbanoutfitters.com/urban/catalog/category.jsp?id=BRANDS&brand=rothco"
url="http://www.zara.com/webapp/wcs/stores/servlet/category/us/en/zara-nam-S2013/358056/Trousers"
url="http://www.zara.com/webapp/wcs/stores/servlet/product/us/en/zara-nam-S2013/358080/1232023/JACKET+WITH+PATCHES"
url="http://www.etsy.com/listing/106835119/micro-stoneware-bowl-white-fine-bone?ref=fp_treasury_1"


get_price(url)



