"""
Created by Zheng Qin
"""
import httplib
import urlparse

def ifPageExists(url):
    host, path = urlparse.urlsplit(url)[1:3]
    found = 0
    try:
        connection = httplib.HTTPConnection(host)  # Make HTTPConnection Object
        connection.request("HEAD", path)
        responseOb = connection.getresponse()      # Grab HTTPResponse Object

        if responseOb.status == 200:
            found = 1
        else:
            print "Status %d %s : %s" % (responseOb.status, responseOb.reason, url)
    except Exception, e:
        print e.__class__,  e, url
    return found

def _test():
    import doctest, ifPageExists
    return doctest.testmod(ifPageExists)

if __name__ == "__main__":
    _test()