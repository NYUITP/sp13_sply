from bottle import route, run
import lxml.html as HTML
import lxml.etree as etree
import difflib
from difflib import SequenceMatcher
import urllib2
import cookielib
from pprint import pprint
import  re
@route('/xpath/<weburl:path>,<imgurl:path>')
def xpath(weburl,imgurl):
    keywordlist=['Euro','USD','$','RMB']
    closest = 0
    imgresults=[]
    keyresults=[]
    imgxpath = ""
    matchfirst=[]
    truexpath = ""
    

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    weburl = "http://"+weburl
    imgurl = "http://"+imgurl
    f = opener.open(weburl)
    s = f.read()
    f.close()

    hdoc = HTML.fromstring(s)
    htree = etree.ElementTree(hdoc)  
   
    image_locations = htree.xpath('//img[@src="'+imgurl+'"]')
    #key_locations = htree.xpath("//*[re:match(text(),'"+keyword+"')]", namespaces={"re": "http://exslt.org/regular-expressions"})
   
    
    for Elem_location in image_locations:
        imgresults.append(htree.getpath(Elem_location))

    for result in imgresults:
        #print "image Xpath:"+ result
        imgxpath = result
        
    for keyword in keywordlist:
        key_locations = htree.xpath("//*[re:match(text(),'"+keyword+"')]", namespaces={"re": "http://exslt.org/regular-expressions"})
        for Elem_location in key_locations:
            keyresults.append(htree.getpath(Elem_location))
        if len(keyresults)!= False:
            break

    for result in keyresults:
        keyxpath = result
        s = difflib.SequenceMatcher(None,imgxpath, keyxpath)
        matchfirst = s.get_matching_blocks()[0]
        close_degree = matchfirst[1]
        if closest < close_degree:
            closest = close_degree
            truexpath = keyxpath

    results=[]
    price=[]
    flag = False
    locations = htree.xpath(truexpath)
    for Elem_location in locations:
        results.append(htree.getpath(Elem_location))
        price.append(Elem_location.text)
        pricestr = str(price)
    pricestr= pricestr[pricestr.find("\'")+1:pricestr.rfind("\'")]
    print pricestr
    if pricestr.isdigit()== True:
            flag = True
    elif pricestr.isalpha()== True:
            flag = True
    else:
           flag = False
        
    if flag == True:
        finalxpath = truexpath[:truexpath.rfind('/')]
        finalxpath = finalxpath+'/*'
        locations = htree.xpath(finalxpath)
        for Elem_location in locations:
            results.append(htree.getpath(Elem_location))
            price.append(Elem_location.text)
              
    return price
    
    
run (host='localhost',port = 8080, debug = True)


