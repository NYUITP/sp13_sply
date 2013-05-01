import sys,re,urllib2,cookielib,urllib
from lxml import etree
import lxml.html as HTML
import lxml.etree as etree
import difflib
from pprint import pprint
from difflib import SequenceMatcher
import  re

# get image xpath
def xpath_imgrequest(imgurl, weburl):
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    f = opener.open(weburl)
    s = f.read()
    f.close()

    hdoc = HTML.fromstring(s)
    htree = etree.ElementTree(hdoc)
    xpaths=[]
    imgresults=[]
    xpath_flag = False
    xpaths = xpath_search(imgurl,weburl)
    for xpath in xpaths:
        image_locations = htree.xpath('//img[contains(@src, "'+xpath+'" )]')
        if len(str(image_locations))>2:
            xpath_flag = True
            break
    if xpath_flag == False:   
        for xpath in xpaths:
            image_locations = htree.xpath('//img[contains(@data-original, "'+xpath+'" )]')
            if len(str(image_locations))>2:
                break
    for Elem_location in image_locations:
        imgresults.append(htree.getpath(Elem_location))
            
    for result in imgresults:
        return result
    
def xpath_search(imgurl,weburl):
    #image_locations =  htree.xpath("//*[re:match(text(),'"+imgurl+"')]", namespaces={"re": "http://exslt.org/regular-expressions"})
    imgurls = []
    imgurltem = imgurl
    imgurls.append(imgurltem)
    imgurltem = imgurl[imgurl.find('.com')+4:]
    imgurls.append(imgurltem)
    imgurltem = imgurl[:imgurl.rfind('/')+1]
    imgurls.append(imgurltem)
    imgurltem = imgurl[imgurl.find('http:')+5:]
    imgurls.append(imgurltem)
    s = difflib.SequenceMatcher(None, imgurl, weburl)
    matchfirst = s.get_matching_blocks()[0]
    position = matchfirst[2]
    imgurltem = imgurl[position-1:]
    imgurls.append(imgurltem)
  
    return imgurls

imgurl1="http://www.mrporter.com/images/products/329468/329468_mrp_in_m2.jpg"
weburl1="http://www.mrporter.com/Shop/List/Paul_Smith_British_Classics?cm_sp=homepage-_-paulsmithm4-_-020413"

weburl2="http://www.urbanexcess.com/c-1190-sweatshirts.aspx"
imgurl2="http://www.urbanexcess.com/images/PRODUCT/icon/01526-320_1.jpg"

imgurl3 = "http://cdn.photojojo.net/store/awesomeness/productImages/spring-break-camera-strap-8984_600.0000001362858205.jpg"
weburl3 = "http://photojojo.com/store/awesomeness/spring-break-camera-strap/"

weburl4 = "http://www.oipolloi.com/apc-cable-knit-pullover-off-white"
imgurl4 = "http://www.oipolloi.com/cache/images/gallery/36236-1--450-auto.jpg"

weburl5 = "http://unionmadegoods.com/SPRING_COLLECTIONS_486.html"
#/Universal_Works_Rose_Print_Button_Down_in_Shirt_in_Orange_8749.html?reframed=1
imgurl5 = "cdn-fsg/unionmade/Images/Products/Rose_Print_Button_Down_in_Shirt_in_Orange_0.jpg"
# find out 1st position different with weburl
weburl6 = "https://canoeonline.net/shop/category/furniture"
imgurl6 = "/img/products/thumbnails/882.jpg"
# rfind('/')
weburl7 = "http://www.lagarconne.com/store/category.htm?sid=24"
imgurl7 = "http://www.lagarconne.com/data/item/19179/imgalt/"
# remove http
weburl8 = "http://www.stevenalan.com/womens-clothing-tops-and-blouses/womens-clothing-tops-and-blouses,default,sc.html"
imgurl8 = "//s7d9.scene7.com/is/image/StevenAlan/S13_3_WST0193_B113_PD?$redesigngrid$"
# [@data-original
weburl9 = "http://www.anthropologie.com/anthro/category/lounge+%26+intimates/clothes-loungewear.jsp"
imgurl9 = "http://images.anthropologie.com/is/image/Anthropologie/26250498_066_b?$$RD2012_category_item$$"
# remove .com
weburl10 = "http://www.urbanexcess.com/c-1176-jeans-chinos.aspx"
imgurl10 = "/images/PRODUCT/icon/8412622_1.jpg"
weburl11 = "http://www.sixpack.fr/shop/"
imgurl11 = "http://www.sixpack.fr/shop/img/p/1680-3591-medium.jpg"

# unknown
weburl12 = "http://www.supremenewyork.com/previews/springsummer2013/top-sweaters/s-s-checkered-henley"
imgurl12 = "http://d2flb1n945r21v.cloudfront.net/production/uploaded/preview/60956/0-KN5_yellow.jpg-zoom_1361187988.jpg"

weburl13 = "http://needsupply.com/mens/brands/billykirk"
imgurl13 = "http://cdn.needsupply.com/media/catalog/product/cache/1/small_image/220x282/e9607dc71bc010050ca2ae6f644b84c1/1/0/1001176_1.jpg"

#imgxpath = xpath_imgrequest(imgurl1,weburl1)

