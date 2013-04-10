#!/usr/bin/env python
import NYUXpath
import NYUschema
import httplib
import urlparse
import json

case_nubmer = 0
right_number = 0
error_number = 0

if __name__=="__main__":
 myfile = open('schema_urls.txt')
 data = myfile.readlines()
 myfile.close()

 for line in data:
   (weburl,imgurl)=line.split('\t')
   ans1= json.loads(NYUschema.get_solution(weburl))
   ans2= json.loads(NYUXpath.main_process(weburl,imgurl))
   print "DOMAIN:%s\tSchema:%s\tXpath:%s" % (weburl.split('/',3)[2],ans1["price"],ans2["price"])
