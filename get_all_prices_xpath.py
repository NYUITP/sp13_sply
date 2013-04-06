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
            print Elem_location.text
            results.append(htree.getpath(Elem_location))
            price.append(Elem_location.text)
            # pricestr = str(price)

    '''
    pricestr= pricestr[pricestr.find("\'")+1:pricestr.rfind("\'")]
    if pricestr.isdigit()== True:
            flag = True
            productprice = pricestr
    elif pricestr.isalpha()== True:
            flag = True
    else:
           flag = False
           pricetem=pricestr.split()
           for tem in pricetem:
               if tem.find(',') >-1:
                    productprice=tem
               elif tem.find('.') >-1:
                    productprice=tem
                    break
    '''
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
# url = "http://www.manufactum.com/sweaters-c193633/"
# url = "http://www.manufactum.com/horse-leather-gentlemans-blouson-p1464993/?c=193631"
# get_price(url)


urls = {
    'http://needsupply.com/womens/breezy-t.html',
    'http://www.manufactum.com/ladies-knitted-camelhair-cardigan-p1449830/',
    'http://www.urbanoutfitters.com/urban/catalog/productdetail.jsp?id=27870609&parentid=M_APP_BUTTONDOWNSHIRTS',
    'http://www.supremenewyork.com/shop/accessories/supreme-spitfire-wheels-set-of-4',
    'http://www.oipolloi.com/nike-air-max-180-og-sail-ultramarine',
    'http://www.sixpack.fr/shop/cut-sew/1679-lucifer-jacket-.html',
    'http://us.asos.com/ASOS-Metal-Top-Keyhole-Round-Sunglasses/x3l4o/?iid=1726298&cid=13494&sh=0&pge=0&pgesize=20&sort=-1&clr=Nude&mporgp=L0FTT1MvQVNPUy1NZXRhbC1Ub3AtS2V5aG9sZS1Sb3VuZC1TdW5nbGFzc2VzL1Byb2Qv',
    'http://www.jcrew.com/womens_category/Collection/sweaters/PRDOVR~37390/37390.jsp',
    'http://www.urbanexcess.com/p-10796-grenson-sharp-calf-brogue-derby-boot-tan.aspx',
    'http://www.anthropologie.com/anthro/product/clothes-dressy-tees/26973164.jsp',
    'http://woodwood.dk/store/product/category-sale-mid_season_sale/eiger-2001-socks-121-mso0001',
    'http://www.stevenalan.com/SHORT-SLEEVED-SINGLE-NEEDLE-SHIRT/848785049544,default,pd.html#cgid=mens-whats-new-new-arrivals&view=all&frmt=ajax&start=0&hitcount=81',
    'http://www.bestmadeco.com/collections/frontpage/products/the-short-sleeve-sweatshirt',
    'http://www.lagarconne.com/store/item.htm?itemid=18391&sid=124&pid=124',
    'http://www.zara.com/webapp/wcs/stores/servlet/product/us/en/zara-nam-S2013/367501/1133509/LINEN+FROCK+COAT+WITH+PRINTED+STRIPES',
    'http://openingceremony.us/products.asp?menuid=2&designerid=1494&productid=77380',
    'https://canoeonline.net/shop/inspect/heath-bud-vase',
    'http://www.unionmadegoods.com/Paraboot_Vigny_Vel_Daim__8937.html',
    'http://www.madewell.com/madewell_category/SHOESANDSANDALS/sandals/PRDOVR~91858/91858.jsp',
    'http://www.mrporter.com/product/317717',
    'http://www.modcloth.com/shop/blouses/je-t-adore-top-in-plus-size',
    'http://www.endclothing.co.uk/brands/saturdays-surf-nyc/saturdays-bowery-chest-s-crew-neck-sweat-105052.html',
    'http://photojojo.com/store/awesomeness/spring-break-camera-strap/',
    'http://www.freepeople.com/clothes-tops/affairs-in-versailles-peplum-27229392/',
    'http://www.theghostlystore.com/collections/frontpage/products/fernando-mastrangelo-beacon-twws'
}

for url in urls:
    get_price(url)
