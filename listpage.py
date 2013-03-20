from bottle import route, run
import lxml.html as HTML
import lxml.etree as etree
import difflib
from difflib import SequenceMatcher
import urllib2
import cookielib
from pprint import pprint
import  re
@route('/xpath/<weburl:path>,<imgurl:path>,<keyword>')
def xpath(weburl,imgurl,keyword):
    closest = 0
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    weburl = "http://"+weburl
    imgurl = "http://"+imgurl
    f = opener.open(weburl)
    s = f.read()
    f.close()

    hdoc = HTML.fromstring(s)
    htree = etree.ElementTree(hdoc)  
   
    image_locations = htree.xpath('//img[@src="'+imgurl+'"]')
    key_locations = htree.xpath("//*[re:match(text(),'"+keyword+"')]", namespaces={"re": "http://exslt.org/regular-expressions"})
    imgresults=[]
    keyresults=[]
    imgxpath = ""
    matchfirst=[]
    truexpath = ""
    for Elem_location in image_locations:
        imgresults.append(htree.getpath(Elem_location))

    for result in imgresults:
        #print "image Xpath:"+ result
        imgxpath = result
        
    for Elem_location in key_locations:
        keyresults.append(htree.getpath(Elem_location))

    for result in keyresults:
        keyxpath = result
        s = difflib.SequenceMatcher(None,imgxpath, keyxpath)
        matchfirst = s.get_matching_blocks()[0]
        close_degree = matchfirst[1]
        if closest < close_degree:
            closest = close_degree
            truexpath = keyxpath

    locations = htree.xpath(truexpath)
    results=[]
    for Elem_location in locations:
        results.append(htree.getpath(Elem_location))
        price = Elem_location.text
    return price
    
    
run (host='localhost',port = 8080, debug = True)


