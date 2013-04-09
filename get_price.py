#from bottle import route, run
import lxml.html as HTML
import lxml.etree as etree
import difflib
from difflib import SequenceMatcher
import urllib2
import cookielib
from pprint import pprint
import  re

#@route('/xpath/<weburl:path>,<imgurl:path>')
#run (host='localhost',port = 8080, debug = True)
def get_price(weburl):
    final = []
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
        final_price=""
        final_symbol=""
        if truexpath.find('script')==-1: 
             print truexpath
             modxpath = []
             modxpath.append(truexpath[:truexpath.rfind('/')])
             modxpath.append(truexpath[:truexpath.rfind('/')+1]+"*")
             #print modxpath
             locations = htree.xpath(truexpath)
             for Elem_location in locations:
                 price = Elem_location.text
                 if price!=None:
                    final_currency = currency_get(price)
                    #final_symbol = currency_get(price)
                    flag = price_check(price)
                    print flag
                    if flag == False:
                        final_price = price_get(price)
                    else:
                        break
             if flag == True:
                 for mod in modxpath:
                     pricestr =""
                     loc = htree.xpath(mod)              
                     for Elem_location in loc:
                        price = Elem_location.text
                        pricestr = pricestr + " " + str(price)
                    
                         
                     price_get(pricestr)
                     if price_get(pricestr)!="No price":
                        final_price = price_get(pricestr)
                        break
                 
            
        print "currency" +final_currency
        print "price" + final_price
        #print truexpath
    return (final_currency, final_price,truexpath)
        

def xpath_filter():
    key=[]
    currencyhead = "€|￥|£|$"
    curhead = "[€,￥,£,$]"
    curhead = unicode(curhead,'utf-8')
    currencyhead = unicode(currencyhead, 'utf-8')
    currencytail = "EUR|Euro|RMB|GBP|JPY|AUD|USD"
    numberstring = "\\d+(?:(?:\\.|,)\\d\\d)?"
    numberstring ="^[0-9\.\,]{1,}"
    #key.append(currencytail)
    key.append("^"+curhead+""+numberstring+""+currencytail+"$")
    #key.append("^"+curhead+""+numberstring+"$")
    #key.append("^"+numberstring+""+currencytail+"$")
    
    return key
    
def currency_get(price):
    pricetem = price.split()
    for tem in pricetem:
        #print tem
        m1 = re.search('^[0-9\.\,]{1,}$',tem)
        m2=re.search('^[A-Za-z]{1,}$',tem)
        m4=re.search('^.[0-9\.\,]{1,}$',tem)
        if m1!= None:
            price = tem
        elif m4 != None:
            price =tem[1:]
            symbol = tem[:1]
        elif m2 != None:
            currency = tem
        elif m1==None and m2==None:
            symbol = tem
        else:
            print "error"
    if currency >-1:
        return currency
    else:
       return symbol
    
def price_check(price):
    currencytail = "EUR|Euro|RMB|RBP|JPY|CAD|AUD|USD"
    curhead = "[€,￥,£,$]"
    curhead = unicode(curhead,'utf-8') 
    flag = False
    currency =""
    symbol = ""
    reg4= curhead+"?.[0-9\,\.]{1,}"
    m4=re.search(reg4,price)
    reg5="^[0-9\.\,]{1,}?.("+currencytail+")$"
    m5=re.search(reg5,price)
    reg6 ="^"+curhead+"[0-9\,\.]{1,}("+currencytail+")$"
    m6=re.search(reg6,price)
    reg1 = "^"+curhead+"$"
    m1=re.search(reg1,price)
    reg2 = "^("+currencytail+")$"
    m2=re.search(reg2,price)
    reg3 = "^"+curhead+"."+"("+currencytail+")$"
    m3 = re.search(reg3,price)
    '''                
    if  m4!=None:
        print "m4" + m4.group(0)
    elif m5!=None:
        print "m5" + m5.group(0)
    elif m6!=None:
        print "m6" + m6.group(0)
    '''
    if m1!=None:
        flag = True
        #print "m1" + m1.group(0)
        symbol = price
    elif m2!= None:
        flag = True
        #print "m2" + m2.group(0)
        currency = price
    elif m3!= None:
        flag = True
        #print "m3" + m3.group(0)
    else:  
        #print "some else"
        flag = False
        symbol = price[:1]
        currency = price[1:]
        #print price
    return flag

def price_get(pri):
    price = "No price"
    pricetem = pri.split()

    for tem in pricetem:
        #print tem
        m1 = re.search('^[0-9\.\,]{1,}$',tem)
        m2=re.search('^[A-Za-z]{1,}$',tem)
        m4=re.search('^.[0-9\.\,]{1,}$',tem)
        if m1!= None:
            price = tem
        elif m4 != None:
            price =tem[1:]
            symbol = tem[:1]
        elif m2 != None:
            currency = tem
        elif m1==None and m2==None:
            symbol = tem
        else:
            print "error"

    return price

    '''
    url = [ "http://www.jcrew.com/AST/Browse/MensBrowse/Men_Shop_By_Category/shirts/washedfavoriteshirts/PRDOVR~14915/14915.jsp",
        "http://hypebeast.com/2009/05/xlarge-x-casio-g-shock-dw-5600/",
        "http://hypebeast.com/2009/05/cheez-2009-summer-new-releases/",
        "http://www.watchismo.com/diesel-dz4160-freak-of-nature-watch.aspx",
        "http://hypebeast.com/2009/05/takashi-kumagai-for-quiksilver-checkered-foulards/",
        "http://men.style.com/news/blog/2009/05/common-projects-strikes-again.html?mbid=rss_upgrdr",
        "http://www.warpweb.jp/shopdetail/008000000001/order/",
        "http://rumplo.com/tees/tee/7110-run-buddha-run",
        "http://rumplo.com/tees/tee/9963-eclectic-method-merch--t shirt--eclectic-method-jetset-remix",
        "http://alterbrooklyn.blogspot.com/2009/05/new-takel-shirts.html",
        "http://gizmodo.com/303906/diesel-rolls-out-oled-watches-two handed-time-telling-returns-from-1970s",
        "http://www.selectism.com/news/2008/12/08/maurice-de-mauriac-chronographs/maurice-de-mauriac-watches-01/",
        "http://goincase.com/products/detail/CL55060",
        "http://goincase.com/products/detail/CL55059",
        "http://amazon.com/dp/B000IXBUEO/?tag=svpply01-20",
        "http://www.chromebagsstore.com/soyuzblkblk.html",
        "http://gearpatrol.com/blog/2009/05/08/rocky-roads-custom-vintage-ford-broncos/",
        "http://www.zappos.com/n/multi_view.cgi?product_id=7419889&color_id=422&view=multi&ref=multi-pic"
        ]
    '''        
url="http://www.oipolloi.com/apc-cable-knit-pullover-off-white"
#url="http://www.urbanoutfitters.com/urban/catalog/productdetail.jsp?id=26503334&parentid=M_APP_SHORTSSWIM_SHORTS"
url="http://www.urbanoutfitters.com/urban/catalog/category.jsp?id=BRANDS&brand=rothco"
#url="http://www.freepeople.com/whats-new-intimates/"
#url = "http://www.manufactum.com/sweaters-c193633/"
#url = "http://www.etsy.com"
#url ="http://www.urbanoutfitters.com/urban/catalog/category.jsp?id=BRANDS&brand=rothco"
#url="http://www.zara.com/webapp/wcs/stores/servlet/category/us/en/zara-nam-S2013/358080/Jackets"
#url="http://www.zara.com/webapp/wcs/stores/servlet/product/us/en/zara-nam-S2013/358080/1232023/JACKET+WITH+PATCHES"
url="http://www.etsy.com/listing/106835119/micro-stoneware-bowl-white-fine-bone?ref=fp_treasury_1"
result = get_price(url)

