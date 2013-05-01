#!/usr/bin/env python
import NYUXpath
import NYUschema
import httplib
import urlparse
import json
from subprocess import Popen, PIPE


case_nubmer = 0
right_number = 0
error_number = 0

if __name__ == "__main__":
    myfile = open('schema&ogp_urls.txt')
    data = myfile.readlines()
    myfile.close()

    for line in data:
        (weburl, imgurl) = line.split(' ')
        ans1 = json.loads(NYUschema.get_solution(weburl))
        ans2 = json.loads(NYUXpath.main_process(weburl, imgurl))
        # casperstring = ["/Users/sebastian/Downloads/n1k0-casperjs-bc0da16/bin/casperjs",
                        # "webcrawlerv7.js", weburl, imgurl.rstrip()]
        # returnval = Popen(casperstring, stdout=PIPE)
        # ans3 = json.loads(returnval.stdout.readline())
        print "DOMAIN:%s\tSchema:%s\tXpath:%s\tSvpply: %s" % (weburl.split('/', 3)[2], ans1["price"], ans2["price"], ans3["price"])
        returnval.stdout.close()
