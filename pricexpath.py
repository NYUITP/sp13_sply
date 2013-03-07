import sys,re,urllib2,cookielib,urllib
from lxml import etree
import lxml.html as HTML
import lxml.etree as etree
import difflib
from pprint import pprint
from difflib import SequenceMatcher



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
        print "image Xpath:"+ result
        imgxpath = result

        return imgxpath

def xpath_request(keyword,weburl):
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    f = opener.open(weburl)
    s = f.read()
    f.close()

    hdoc = HTML.fromstring(s)
    htree = etree.ElementTree(hdoc)
    locations = htree.xpath('//*[text()="'+keyword+'"]')
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
        if closest < close_degree:
            closest = close_degree
            truexpath = xpath

    return truexpath

        

   
imgurl="http://images.manufactum.de/manufactum/thumbs_188/27256_1.jpg"
weburl="http://www.manufactum.com/trousers-skirts-robes-c193632/"
keyword = "availability"
imgxpath = xpath_imgrequest(imgurl,weburl)
#print imgxpath
sta=[]
sta=xpath_request(keyword,weburl)
#for status in sta:
#    print status

print keyword + "  XPath:", xpath_compare(imgxpath, sta)


