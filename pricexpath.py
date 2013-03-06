import sys,re,urllib2,cookielib,urllib
from lxml import etree
import lxml.html as HTML
import lxml.etree as etree
import difflib
from pprint import pprint
from difflib import SequenceMatcher


           
#url = "http://www.manufactum.com/ladies-elysian-duffle-coat-p1465087/?a=74015"
url= "http://www.manufactum.com/trousers-skirts-robes-c193632/"
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookielib.CookieJar()))
f = opener.open(url)
s = f.read()
f.close()

hdoc = HTML.fromstring(s)
htree = etree.ElementTree(hdoc)
#myelements_locations = htree.xpath("//*[text()='Accessories']")
#myelements_locations = htree.xpath('//a[@href="http://www.manufactum.com/nightwear-c193630/"]')
image_locations = htree.xpath('//img[@src="http://images.manufactum.de/manufactum/thumbs_188/27256_1.jpg"]')
price_locations = htree.xpath("//*[text()='availability']")

imgresults=[]
priceresults=[]
for Elem_location in image_locations:
    imgresults.append(htree.getpath(Elem_location))
for result in imgresults:
   print "image Xpath:"+ result
   imgxpath = result;


for Elem_location in price_locations:
    priceresults.append(htree.getpath(Elem_location))

for result in priceresults:
    print "Status Xpath:"+ result
    s = difflib.SequenceMatcher(None, imgxpath, result)
    pprint(s.get_matching_blocks())




 

