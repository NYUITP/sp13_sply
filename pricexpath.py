import sys,re,urllib2,cookielib,urllib
from lxml import etree
import lxml.html as HTML
import lxml.etree as etree
import difflib
from pprint import pprint
from difflib import SequenceMatcher
import  re



def xpath_imgrequest(imgurl, weburl):
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    f = opener.open(weburl)
    s = f.read()
    f.close()

    hdoc = HTML.fromstring(s)
    htree = etree.ElementTree(hdoc)
   
    image_locations = htree.xpath('//img[@src="'+imgurl+'"]')
    #image_locations = htree.xpath('//img[@src="http://images.manufactum.de/manufactum/thumbs_188/27256_1.jpg"]')
    imgresults=[]    
 
    for Elem_location in image_locations:
        imgresults.append(htree.getpath(Elem_location))

    for result in imgresults:
        #print "image Xpath:"+ result
        imgxpath = result
        return imgxpath

def xpath_request(keyword,weburl):
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    f = opener.open(weburl)
    s = f.read()
    f.close()

    hdoc = HTML.fromstring(s)
    htree = etree.ElementTree(hdoc)
    locations = htree.xpath("//*[re:match(text(),'"+keyword+"')]", namespaces={"re": "http://exslt.org/regular-expressions"})
    #locations = htree.xpath("//*[re:match(text(),'Euro')]", namespaces={"re": "http://exslt.org/regular-expressions"})
    

    results=[]
    for Elem_location in locations:
        results.append(htree.getpath(Elem_location))
        
    for result in results:
        return results
    

 
def xpath_compare(imagexpath, canxpath=[]):
    closest=0

    for xpath in canxpath:
        
        s = difflib.SequenceMatcher(None, imagexpath, xpath)
        matchfirst = s.get_matching_blocks()[0]
        close_degree = matchfirst[2]
        #print "close degree: ", close_degree
        if closest < close_degree:
            closest = close_degree
            truexpath = xpath
    return truexpath
            
def info_request(weburl,xpath):
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    f = opener.open(weburl)
    s = f.read()
    f.close()

    hdoc = HTML.fromstring(s)
    htree = etree.ElementTree(hdoc)
    
    locations = htree.xpath(xpath)
    results=[]
    for Elem_location in locations:
        results.append(htree.getpath(Elem_location))
        print Elem_location.text
        print Elem_location.attrib
    for res in results:
        print res
        
        
    
    
    
        

   
imgurl="http://images.manufactum.de/manufactum/thumbs_188/84498_1.jpg"
weburl="http://www.manufactum.com/sweaters-c193633/"
#keyword = "availability"
keyword = "Euro"
imgxpath = xpath_imgrequest(imgurl,weburl)
print "image Xpath:  "+ imgxpath
sta=[]
sta=xpath_request(keyword,weburl)
#for status in sta:
#    print status
xpath = xpath_compare(imgxpath, sta)
print info_request(weburl, xpath)



