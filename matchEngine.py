import get_price
import get_solution
import httplib
import urlparse


case_nubmer = 0
right_number = 0
error_number = 0


# get all results for all urls, get all solutions, check if equal. Return accuracy rate.
# read in urls from "web_urls.txt"
def check_results(filename):
    file = open(filename)
    while 1:
        urls = file.readlines(100000)
        if not urls:
            break
        for url in urls:
            # get solution could be a case file or a function like schema
            if (get_price.get_price(url,) == get_solution.get_solution(url,)):
                case_nubmer = case_nubmer + 1
                right_number = right_number + 1
                print "Good!"
            else:
                case_nubmer = case_nubmer + 1
                print "******************WARNING*************************"
                print url,
                print get_price.get_price(url,)
                print get_solution.get_solution(url,)
                print "**************************************************"
        accracy_rate = right_number/case_nubmer
    return accracy_rate


            # return (final_currency, final_price, truexpath)
            # get_price.get_price(url,)
            # add return to array
            # results.append(get_price.get_price(url,))
            # results[].add
    # file.close()
    # print results
    # return results
# get_results('web_urls.txt')
# def get_solution(filename):
#     file = open(filename)
#     while 1:
#         lines = file.readline(100000)
#         if not lines:
#             break
#         for line in lines:
#             solutions.append(list(map(line)))
    # file.close()
    # return solutions
# def match_engine():
#     for
# calculate accracy rate, error rate
# def statistics():
#     pass


# check if url is product page
def is_url_product_page():
    pass


# check if url avaliable
def is_url_avaliable(url):
    host, path = urlparse.urlsplit(url)[1:3]
    found = 0
    try:
        connection = httplib.HTTPConnection(host)  # Make HTTPConnection Object
        connection.request("HEAD", path)
        responseOb = connection.getresponse()  # Grab HTTPResponse Object

        if responseOb.status == 200:
            found = 1
        else:
            print "Status %d %s : %s" % (responseOb.status, responseOb.reason, url)
    except Exception, e:
        print e.__class__,  e, url
    return found
