import sys,re,urllib2,cookielib,urllib
from lxml import etree
import lxml.html as HTML
import lxml.etree as etree
import difflib
from pprint import pprint
from difflib import SequenceMatcher
import  re
from cssformat import format

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


def css_reqest(weburl, css_keyword):
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    f = opener.open(weburl)
    s = f.read()
    f.close()
    keyword = "stylesheet"
    hdoc = HTML.fromstring(s)
    htree = etree.ElementTree(hdoc)
   
    image_locations = htree.xpath('//link[@rel="'+keyword+'"]')
    imgresults=[]
    css_xpaths=[]   
 
    for Elem_location in image_locations:
        imgresults.append(htree.getpath(Elem_location))
        css_xpath =str(Elem_location.attrib)
        temp1 = ": '"
        temp2 = ".css"
        css_xpath = css_xpath[css_xpath.find(temp1)+3:css_xpath.find(temp2)]+temp2
        print css_xpath
        css_xpaths.append(css_xpath)
        return css_xpaths

def css_analyzer(css_url, keyword):
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
    f = opener.open(css_url)
    s = f.read()
    format(s)
    f.close()
    temp1 = "currency-symbol{"
    temp2 = "}"
    css_targets=[]
    
    css_targets.append(s[s.find(temp1):s.find(temp2)])
    for css_target in css_targets:
        print css_target
    
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
    #locations = htree.xpath("")
    
    #for ele in htree.iter("strong"):
    #    print ("%s-%s"(ele.tag, ele.text))
    
    results=[]
    for Elem_location in locations:
        results.append(htree.getpath(Elem_location))
        #print Elem_location.text
        #print Elem_location.attrib
        #print Elem_location.tag
        if Elem_location.tag.find("strong")!= -1:
            print "True"
        elif Elem_location.tag.find("bold")!=-1:
            print "True"
        else:
            print "False"
    #for res in results:
       # print res
        
        
    
    
    
        

   
#imgurl="http://img2.etsystatic.com/010/0/6159037/il_570xN.437136834_qr6f.jpg"
weburl="http://www.etsy.com/listing/92141214/spring-wreath-front-door-decor-mothers?ref=br_feed_1"
#weburl="http://www.manufactum.com/shetland-chunky-pullover-p1460026/?c=193633"
imgurl="http://images.manufactum.de/manufactum/produktdetail/84498_1.jpg"
#keyword = "availability"
#keyword = "Euro"
#imgxpath = xpath_imgrequest(imgurl,weburl)
#print "image Xpath:  "+ imgxpath
#sta=[]
#sta=xpath_request(keyword,weburl)
#for status in sta:
#    print status
#xpath = xpath_compare(imgxpath, sta)
#print info_request(weburl, xpath)

css_paths=[]
css_paths = css_reqest(weburl, "stylesheet")
for css_path in css_paths:
    print css_path
    css_analyzer(css_path, "currency")
    

