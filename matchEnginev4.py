#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import NYUXpath
import NYUschema
import httplib
import urlparse
import json
from subprocess import Popen, PIPE


if __name__=="__main__":
 #myfile = open('schema_urls.txt')
 myfile = open('JsRunner_urls6.txt')
 #myfile = open('schemaogp_urls2.txt')
 data = myfile.readlines()
 myfile.close()
 n_correct=0 
 n_notfound=0
 for line in data:
   (weburl,imgurl,price,currency)=line.split('\t')
   #ans1= json.loads(NYUschema.get_solution(weburl))
   #ans2= json.loads(NYUXpath.main_process(weburl,imgurl))
   casperstring= ["/Users/sebastian/Downloads/n1k0-casperjs-bc0da16/bin/casperjs", "webcrawlerv7.js" , weburl,imgurl.rstrip()]  
   returnval= Popen(casperstring,stdout=PIPE) 
   ans3 = json.loads(returnval.stdout.readline())
   if ans3:
   #print "DOMAIN:%s\tSchema:%s\tXpath:%s\tSvpply: %s" % (weburl.split('/',3)[2],ans1["price"],ans2["price"],ans3["price"])
   #print "DOMAIN:%s\tSchema:%s\tSvpply: %s" % (weburl.split('/',3)[2],ans1["price"],ans3["price"])
    print "SITE:%s\tScriptPrice: %s\tDBPrice:%s\tCorrect:%s" % (weburl,ans3["price"],price,('Yes' if ans3["price"]==price else 'No'))
   returnval.stdout.close()
   if ans3["price"] == price:
       n_correct+=1
   else:
       if ans3["price"] == "-1":
        n_notfound+=1 
 print "Accuracy rate of total set: %.2F" % (float(n_correct)/len(data))
 print "Accuracy rate of found images: %.2F" % (float(n_correct)/(len(data) - n_notfound))
