import os


if __name__ == "__main__":
    myfile = open('schema&ogp_urls.txt')
    for line in myfile:
        # urls = line.split('\t')
        # print weburl.rstrip()
        casper = "casperjs webcrawlerv7.js {0}".format(line)
        # cmd = (casper + urls)
        # print casper
        # print os.popen('casperjs webcrawlerv7.js ' + urls).read()
        print os.popen(casper).read()
        # print main_process(weburl,imgurl)
    myfile.close()
