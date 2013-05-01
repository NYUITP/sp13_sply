import sys,re,urllib2,cookielib,urllib
from lxml import etree
import lxml.html as HTML
import lxml.etree as etree
import difflib
from pprint import pprint
from difflib import SequenceMatcher
import  re
# get shortest xpath distance. Return xpath with closest xpath distance.
# input string imagexpath and list all pricexpath/status xpath; output list of price/status xpath with closest xpath distance. 
def xpath_compare(imagexpath, canxpath=[]):
    closest=0
    close_list = []
    for xpath in canxpath:
        s = difflib.SequenceMatcher(None, imagexpath, xpath)
        matchfirst = s.get_matching_blocks()[0]
        close_degree = matchfirst[2]
        if closest < close_degree:
            closest = close_degree
            truexpath = xpath
    #print closest
    for xpath in canxpath:
        s = difflib.SequenceMatcher(None, imagexpath, xpath)
        matchfirst = s.get_matching_blocks()[0]
        close_degree = matchfirst[2]
        if closest == close_degree:
            close_list.append(xpath)
            
    #print close_list
    return close_list
            
    
      




