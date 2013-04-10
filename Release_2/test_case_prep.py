import csv


def test_prep(filename):
    file = open(filename)
    while 1:
        urls = file.readlines(100000)
        if not urls:
            break
        for url in urls:
        	url.split(",")
        	print url,
            # get solution could be a case file or a function like schema
            # if (get_price.get_price(url,) == get_solution.get_solution(url,)):
            #     case_nubmer = case_nubmer + 1
            #     right_number = right_number + 1
                # print "Good!"
        #     else:
        #         case_nubmer = case_nubmer + 1
        #         print "******************WARNING*************************"
        #         print url,
        #         print get_price.get_price(url,)
        #         print get_solution.get_solution(url,)
        #         print "**************************************************"
        # accracy_rate = right_number/case_nubmer
    # return accracy_rate


test_prep('web_urls&img_urls.csv')