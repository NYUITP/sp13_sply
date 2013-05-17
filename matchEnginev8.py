#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import httplib
import urlparse
import json
from subprocess import Popen, PIPE
import sys

if __name__=="__main__":
  
 myfile = open(sys.argv[2])
 data = myfile.readlines()
 myfile.close()
 results=[]
 n_correct=0 
 n_notfound=0
 html_part1="<!DOCTYPE html> <html> <body><p><b>Svpply</b></p>"

 html_part2="<p>Accuracy rate of total set: %.2F </p> <p>Accuracy rate of found images: %.2F</p></p><table border=1> \
<tr> \
  <td>Website</td> \
  <td>imgurl</td> \
  <td>Price</td> \
  <td>DB Price</td> \
  <td>Correct</td> \
  <td>Debug</td> \
</tr> "
 html_partf = "</table></body></html>"
 html_line = "<tr> <td> <a href=%s >Site </a> </td> <td> <a href=%s>Image</a></td> <td>%s</td> <td>%s</td> <td>%s</td> <td>%s</td></tr>"
 for line in data:
   (weburl,imgurl,price,currency)=line.split('\t')
   casperstring= ["/Users/sebastian/Downloads/n1k0-casperjs-bc0da16/bin/casperjs", sys.argv[1] , weburl,imgurl.rstrip()]  
   returnval= Popen(casperstring,stdout=PIPE) 
   ans3 = json.loads(returnval.stdout.readline())
   if ans3:
    #print "SITE:%s\tScriptPrice: %s\tDBPrice:%s\tCorrect:%s" % (weburl,ans3["price"],price,('Yes' if ans3["price"]==price else 'No'))
    results.append([weburl,imgurl,ans3["price"],price]) 
   returnval.stdout.close()
   if ans3["price"] == price:
       n_correct+=1.0
   else:
       if ans3["price"] == "-1":
        n_notfound+=1.0 
 
 ### Lets generate html###
 print html_part1
 print html_part2 % ((n_correct/float(len(data))), (n_correct/(float(len(data)) - n_notfound)))
 for line in results:
   print html_line % (line[0],line[1],line[2],line[3],('Yes' if line[2]==line[3] else 'No'),"<a href=http://www.yahoo.com>Debug</a>")
 print html_partf


